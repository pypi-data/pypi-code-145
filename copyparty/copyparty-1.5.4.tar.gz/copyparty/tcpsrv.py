# coding: utf-8
from __future__ import print_function, unicode_literals

import os
import re
import socket
import sys

from .__init__ import ANYWIN, PY2, TYPE_CHECKING, VT100, unicode
from .stolen.qrcodegen import QrCode
from .util import (
    E_ACCESS,
    E_ADDR_IN_USE,
    E_ADDR_NOT_AVAIL,
    E_UNREACH,
    Netdev,
    min_ex,
    sunpack,
    termsize,
)

if TYPE_CHECKING:
    from .svchub import SvcHub

if not hasattr(socket, "IPPROTO_IPV6"):
    setattr(socket, "IPPROTO_IPV6", 41)


class TcpSrv(object):
    """
    tcplistener which forwards clients to Hub
    which then uses the least busy HttpSrv to handle it
    """

    def __init__(self, hub ):
        self.hub = hub
        self.args = hub.args
        self.log = hub.log

        # mp-safe since issue6056
        socket.setdefaulttimeout(120)

        self.stopping = False
        self.srv  = []
        self.bound   = []
        self.nsrv = 0
        self.qr = ""
        pad = False
        ok   = {}
        for ip in self.args.i:
            if ip == "::":
                if socket.has_ipv6:
                    ips = ["::", "0.0.0.0"]
                    dual = True
                else:
                    ips = ["0.0.0.0"]
                    dual = False
            else:
                ips = [ip]
                dual = False

            for ipa in ips:
                ok[ipa] = []

            for port in self.args.p:
                successful_binds = 0
                try:
                    for ipa in ips:
                        try:
                            self._listen(ipa, port)
                            ok[ipa].append(port)
                            successful_binds += 1
                        except:
                            if dual and ":" in ipa:
                                t = "listen on IPv6 [{}] failed; trying IPv4 {}...\n{}"
                                self.log("tcpsrv", t.format(ipa, ips[1], min_ex()), 3)
                                pad = True
                                continue

                            # binding 0.0.0.0 after :: fails on dualstack
                            # but is necessary on non-dualstakc
                            if successful_binds:
                                continue

                            raise

                except Exception as ex:
                    if self.args.ign_ebind or self.args.ign_ebind_all:
                        t = "could not listen on {}:{}: {}"
                        self.log("tcpsrv", t.format(ip, port, ex), c=3)
                        pad = True
                    else:
                        raise

        if not self.srv and not self.args.ign_ebind_all:
            raise Exception("could not listen on any of the given interfaces")

        if pad:
            self.log("tcpsrv", "")

        eps = {
            "127.0.0.1": Netdev("127.0.0.1", 0, "", "local only"),
            "::1": Netdev("::1", 0, "", "local only"),
        }
        nonlocals = [x for x in self.args.i if x not in [k.split("/")[0] for k in eps]]
        if nonlocals:
            try:
                self.netdevs = self.detect_interfaces(self.args.i)
            except:
                t = "failed to discover server IP addresses\n"
                self.log("tcpsrv", t + min_ex(), 3)
                self.netdevs = {}

            eps.update({k.split("/")[0]: v for k, v in self.netdevs.items()})
            if not eps:
                for x in nonlocals:
                    eps[x] = Netdev(x, 0, "", "external")
        else:
            self.netdevs = {}

        # keep IPv6 LL-only nics
        ll_ok  = set()
        for ip, nd in self.netdevs.items():
            if not ip.startswith("fe80"):
                continue

            just_ll = True
            for ip2, nd2 in self.netdevs.items():
                if nd == nd2 and ":" in ip2 and not ip2.startswith("fe80"):
                    just_ll = False

            if just_ll or self.args.ll:
                ll_ok.add(ip.split("/")[0])

        qr1   = {}
        qr2   = {}
        msgs = []
        title_tab    = {}
        title_vars = [x[1:] for x in self.args.wintitle.split(" ") if x.startswith("$")]
        t = "available @ {}://{}:{}/  (\033[33m{}\033[0m)"
        for ip, desc in sorted(eps.items(), key=lambda x: x[1]):
            if ip.startswith("fe80") and ip not in ll_ok:
                continue

            for port in sorted(self.args.p):
                if (
                    port not in ok.get(ip, [])
                    and port not in ok.get("::", [])
                    and port not in ok.get("0.0.0.0", [])
                ):
                    continue

                proto = " http"
                if self.args.http_only:
                    pass
                elif self.args.https_only or port == 443:
                    proto = "https"

                hip = "[{}]".format(ip) if ":" in ip else ip
                msgs.append(t.format(proto, hip, port, desc))

                is_ext = "external" in unicode(desc)
                qrt = qr1 if is_ext else qr2
                try:
                    qrt[ip].append(port)
                except:
                    qrt[ip] = [port]

                if not self.args.wintitle:
                    continue

                if port in [80, 443]:
                    ep = ip
                else:
                    ep = "{}:{}".format(ip, port)

                hits = []
                if "pub" in title_vars and is_ext:
                    hits.append(("pub", ep))

                if "pub" in title_vars or "all" in title_vars:
                    hits.append(("all", ep))

                for var in title_vars:
                    if var.startswith("ip-") and ep.startswith(var[3:]):
                        hits.append((var, ep))

                for tk, tv in hits:
                    try:
                        title_tab[tk][tv] = 1
                    except:
                        title_tab[tk] = {tv: 1}

        if msgs:
            for t in msgs:
                self.log("tcpsrv", t)

        if self.args.wintitle:
            self._set_wintitle(title_tab)
        else:
            print("\n", end="")

        if self.args.qr or self.args.qrs:
            self.qr = self._qr(qr1, qr2)

    def _listen(self, ip , port )  :
        ipv = socket.AF_INET6 if ":" in ip else socket.AF_INET
        srv = socket.socket(ipv, socket.SOCK_STREAM)

        if not ANYWIN or self.args.reuseaddr:
            srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        srv.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        srv.settimeout(None)  # < does not inherit, ^ opts above do

        try:
            srv.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, False)
        except:
            pass  # will create another ipv4 socket instead

        try:
            srv.bind((ip, port))
            self.srv.append(srv)
        except (OSError, socket.error) as ex:
            if ex.errno in E_ADDR_IN_USE:
                e = "\033[1;31mport {} is busy on interface {}\033[0m".format(port, ip)
            elif ex.errno in E_ADDR_NOT_AVAIL:
                e = "\033[1;31minterface {} does not exist\033[0m".format(ip)
            else:
                raise
            raise Exception(e)

    def run(self)  :
        all_eps = [x.getsockname()[:2] for x in self.srv]
        bound   = []
        srvs  = []
        for srv in self.srv:
            ip, port = srv.getsockname()[:2]
            try:
                srv.listen(self.args.nc)
            except:
                if ip == "0.0.0.0" and ("::", port) in bound:
                    # dualstack
                    srv.close()
                    continue

                if ip == "::" and ("0.0.0.0", port) in all_eps:
                    # no ipv6
                    srv.close()
                    continue

                raise

            bound.append((ip, port))
            srvs.append(srv)
            fno = srv.fileno()
            hip = "[{}]".format(ip) if ":" in ip else ip
            msg = "listening @ {}:{}  f{} p{}".format(hip, port, fno, os.getpid())
            self.log("tcpsrv", msg)
            if self.args.q:
                print(msg)

            self.hub.broker.say("listen", srv)

        self.srv = srvs
        self.bound = bound
        self.nsrv = len(srvs)
        self.hub.broker.say("set_netdevs", self.netdevs)

    def shutdown(self)  :
        self.stopping = True
        try:
            for srv in self.srv:
                srv.close()
        except:
            pass

        self.log("tcpsrv", "ok bye")

    def detect_interfaces(self, listen_ips )   :
        from .stolen.ifaddr import get_adapters

        nics = get_adapters(True)
        eps   = {}
        for nic in nics:
            for nip in nic.ips:
                ipa = nip.ip[0] if ":" in str(nip.ip) else nip.ip
                sip = "{}/{}".format(ipa, nip.network_prefix)
                nd = Netdev(sip, nic.index or 0, nic.nice_name, "")
                eps[sip] = nd
                try:
                    idx = socket.if_nametoindex(nd.name)
                    if idx and idx != nd.idx:
                        t = "netdev idx mismatch; ifaddr={} cpython={}"
                        self.log("tcpsrv", t.format(nd.idx, idx), 3)
                        nd.idx = idx
                except:
                    pass

        if "0.0.0.0" not in listen_ips and "::" not in listen_ips:
            eps = {k: v for k, v in eps.items() if k.split("/")[0] in listen_ips}

        try:
            ext_devs = list(self._extdevs_nix())
            ext_ips = [k for k, v in eps.items() if v.name in ext_devs]
            ext_ips = [x.split("/")[0] for x in ext_ips]
            if not ext_ips:
                raise Exception()
        except:
            rt = self._defroute()
            ext_ips = [rt] if rt else []

        for lip in listen_ips:
            if not ext_ips or lip not in ["0.0.0.0", "::"] + ext_ips:
                continue

            desc = "\033[32mexternal"
            ips = ext_ips if lip in ["0.0.0.0", "::"] else [lip]
            for ip in ips:
                ip = next((x for x in eps if x.startswith(ip + "/")), "")
                if ip and "external" not in eps[ip].desc:
                    eps[ip].desc += ", " + desc

        return eps

    def _extdevs_nix(self)    :
        with open("/proc/net/route", "rb") as f:
            next(f)
            for ln in f:
                r = ln.decode("utf-8").strip().split()
                if r[1] == "0" * 8 and int(r[3], 16) & 2:
                    yield r[0]

    def _defroute(self)  :
        ret = ""
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for ip in [
            "10.254.39.23",
            "172.31.39.23",
            "192.168.39.23",
            "239.254.39.23",
            "169.254.39.23",
            # could add 1.1.1.1 as a final fallback
            # but external connections is kinshi
        ]:
            try:
                s.connect((ip, 1))
                ret = s.getsockname()[0]
                break
            except (OSError, socket.error) as ex:
                if ex.errno in E_ACCESS:
                    self.log("tcpsrv", "eaccess {} (trying next)".format(ip))
                elif ex.errno not in E_UNREACH:
                    self.log("tcpsrv", "route lookup failed; err {}".format(ex.errno))

        s.close()
        return ret

    def _set_wintitle(self, vs   )  :
        vs["all"] = vs.get("all", {"Local-Only": 1})
        vs["pub"] = vs.get("pub", vs["all"])

        vs2 = {}
        for k, eps in vs.items():
            filt = {ep: 1 for ep in eps if ":" not in ep}
            have = set(filt)
            for ep in sorted(eps):
                ip = ep.split(":")[0]
                if ip not in have:
                    have.add(ip)
                    filt[ep] = 1

            lo = [x for x in filt if x.startswith("127.")]
            if len(filt) > 3 and lo:
                for ip in lo:
                    filt.pop(ip)

            vs2[k] = filt

        title = ""
        vs = vs2
        for p in self.args.wintitle.split(" "):
            if p.startswith("$"):
                seps = list(sorted(vs.get(p[1:], {"(None)": 1}).keys()))
                p = ", ".join(seps[:3])
                if len(seps) > 3:
                    p += ", ..."

            title += "{} ".format(p)

        print("\033]0;{}\033\\\n".format(title), file=sys.stderr, end="")
        sys.stderr.flush()

    def _qr(self, t1  , t2  )  :
        ip = None
        ips = list(t1) + list(t2)
        qri = self.args.qri
        if self.args.zm and not qri:
            name = self.args.name + ".local"
            t1[name] = next(v for v in (t1 or t2).values())
            ips = [name] + ips

        for ip in ips:
            if ip.startswith(qri) or qri == ".":
                break
            ip = ""

        if not ip:
            # maybe /bin/ip is missing or smth
            ip = qri

        if not ip:
            return ""

        if ":" in ip:
            ip = "[{}]".format(ip)

        if self.args.http_only:
            https = ""
        elif self.args.https_only:
            https = "s"
        else:
            https = "s" if self.args.qrs else ""

        ports = t1.get(ip, t2.get(ip, []))
        dport = 443 if https else 80
        port = "" if dport in ports or not ports else ":{}".format(ports[0])
        txt = "http{}://{}{}/{}".format(https, ip, port, self.args.qrl)

        btxt = txt.encode("utf-8")
        if PY2:
            btxt = sunpack(b"B" * len(btxt), btxt)

        fg = self.args.qr_fg
        bg = self.args.qr_bg
        pad = self.args.qrp
        zoom = self.args.qrz
        qrc = QrCode.encode_binary(btxt)
        if zoom == 0:
            try:
                tw, th = termsize()
                tsz = min(tw // 2, th)
                zoom = 1 if qrc.size + pad * 2 >= tsz else 2
            except:
                zoom = 1

        qr = qrc.render(zoom, pad)
        if not VT100:
            return "{}\n{}".format(txt, qr)

        halfc = "\033[40;48;5;{0}m{1}\033[47;48;5;{2}m"
        if not fg:
            halfc = "\033[0;40m{1}\033[0;47m"

        def ansify(m )  :
            return halfc.format(fg, " " * len(m.group(1)), bg)

        if zoom > 1:
            qr = re.sub("(█+)", ansify, qr)

        qr = qr.replace("\n", "\033[K\n") + "\033[K"  # win10do
        cc = " \033[0;38;5;{0};47;48;5;{1}m" if fg else " \033[0;30;47m"
        t = cc + "\n{2}\033[999G\033[0m\033[J"
        t = t.format(fg, bg, qr)
        if ANYWIN:
            # prevent color loss on terminal resize
            t = t.replace("\n", "`\n`")

        return txt + t
