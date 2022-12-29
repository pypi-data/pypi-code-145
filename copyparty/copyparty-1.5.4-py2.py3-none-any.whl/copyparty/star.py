# coding: utf-8
from __future__ import print_function, unicode_literals

import stat
import tarfile

from queue import Queue

from .bos import bos
from .sutil import StreamArc, errdesc
from .util import Daemon, fsenc, min_ex

class QFile(object):  # inherit io.StringIO for painful typing
    """file-like object which buffers writes into a queue"""

    def __init__(self)  :
        self.q  = Queue(64)
        self.bq  = []
        self.nq = 0

    def write(self, buf )  :
        if buf is None or self.nq >= 240 * 1024:
            self.q.put(b"".join(self.bq))
            self.bq = []
            self.nq = 0

        if buf is None:
            self.q.put(None)
        else:
            self.bq.append(buf)
            self.nq += len(buf)


class StreamTar(StreamArc):
    """construct in-memory tar file from the given path"""

    def __init__(
        self,
        log ,
        fgen    ,
        **kwargs 
    ):
        super(StreamTar, self).__init__(log, fgen)

        self.ci = 0
        self.co = 0
        self.qfile = QFile()
        self.errf   = {}

        # python 3.8 changed to PAX_FORMAT as default,
        # waste of space and don't care about the new features
        fmt = tarfile.GNU_FORMAT
        self.tar = tarfile.open(fileobj=self.qfile, mode="w|", format=fmt)  # type: ignore

        Daemon(self._gen, "star-gen")

    def gen(self)    :
        try:
            while True:
                buf = self.qfile.q.get()
                if not buf:
                    break

                self.co += len(buf)
                yield buf

            yield None
        finally:
            if self.errf:
                bos.unlink(self.errf["ap"])

    def ser(self, f  )  :
        name = f["vp"]
        src = f["ap"]
        fsi = f["st"]

        if stat.S_ISDIR(fsi.st_mode):
            return

        inf = tarfile.TarInfo(name=name)
        inf.mode = fsi.st_mode
        inf.size = fsi.st_size
        inf.mtime = fsi.st_mtime
        inf.uid = 0
        inf.gid = 0

        self.ci += inf.size
        with open(fsenc(src), "rb", 512 * 1024) as fo:
            self.tar.addfile(inf, fo)

    def _gen(self)  :
        errors = []
        for f in self.fgen:
            if "err" in f:
                errors.append((f["vp"], f["err"]))
                continue

            try:
                self.ser(f)
            except:
                ex = min_ex(5, True).replace("\n", "\n-- ")
                errors.append((f["vp"], ex))

        if errors:
            self.errf, txt = errdesc(errors)
            self.log("\n".join(([repr(self.errf)] + txt[1:])))
            self.ser(self.errf)

        self.tar.close()
        self.qfile.write(None)
