#!/usr/local/bin python3
# -*- coding: utf-8 -*-

"""
    created by FAST-DEV 2021/4/6
"""

from fast_tracker import agent, config
from fast_tracker.trace import ID
from fast_tracker.trace.carrier import Carrier
from fast_tracker.trace.segment import Segment, SegmentRef
from fast_tracker.trace.snapshot import Snapshot
from fast_tracker.trace.span import Span, Kind, NoopSpan, EntrySpan, ExitSpan
from fast_tracker.utils.counter import SpanCounter

try:  # attempt to use async-local instead of thread-local context and spans
    import contextvars

    __local = contextvars.ContextVar("local")
    __spans = contextvars.ContextVar("spans")  # this needs to be a per-task variable, can't be part of __local
    _spans = __spans.get
    _spans_set = __spans.set  # pyre-ignore

    class AsyncLocal:
        pass

    def _local():
        try:
            return __local.get()

        except LookupError:
            local = AsyncLocal()
            __local.set(local)

            return local

    def _spans_dup():
        spans = __spans.get()[:]
        __spans.set(spans)

        return spans


except ImportError:
    import threading

    __local = threading.local()

    def _local():
        return __local

    def _spans():
        return __local.spans

    def _spans_set(spans):
        __local.spans = spans

    _spans_dup = _spans


class SpanContext(object):
    def __init__(self):
        self.segment = Segment()  # type: Segment
        self._sid = SpanCounter()
        self._correlation = {}  # type: dict
        self._nspans = 0

    def new_local_span(self, op: str) -> Span:
        span = self.ignore_check(op, Kind.Local)
        if span is not None:
            return span

        spans = _spans_dup()
        parent = spans[-1] if spans else None  # type: Span

        return Span(
            context=self,
            sid=self._sid.next(),
            pid=parent.sid if parent else "",
            op=op,
            kind=Kind.Local,
        )

    def new_entry_span(self, op: str, carrier: "Carrier" = None) -> Span:
        span = self.ignore_check(op, Kind.Entry)
        if span is not None:
            return span

        spans = _spans_dup()
        parent = spans[-1] if spans else None  # type: Span

        parent_id = ""
        if parent:
            parent_id = parent.sid
        elif carrier and carrier.span_id:  # 当跨服务调用的时候，carrier.span_id等都有值，span_id为上一个服务调用此服务的span_id
            parent_id = carrier.span_id

        span = (
            parent
            if parent is not None and parent.kind.is_entry
            else EntrySpan(
                context=self,
                sid=self._sid.next(),
                pid=parent_id,
            )
        )
        span.op = op

        if carrier is not None and carrier.is_valid:
            span.extract(carrier=carrier)

        return span

    def new_exit_span(self, op: str, peer: str) -> Span:
        span = self.ignore_check(op, Kind.Exit)
        if span is not None:
            return span

        spans = _spans_dup()
        parent = spans[-1] if spans else None  # type: Span

        span = (
            parent
            if parent is not None and parent.kind.is_exit
            else ExitSpan(
                context=self,
                sid=self._sid.next(),
                pid=parent.sid if parent else "",
                op=op,
                peer=peer,
            )
        )

        return span

    def ignore_check(self, op: str, kind: Kind):
        if config.RE_IGNORE_PATH.match(op):
            return NoopSpan(
                context=NoopContext(),
                kind=kind,
            )

        return None

    def start(self, span: Span):
        self._nspans += 1
        spans = _spans()
        if span not in spans:
            spans.append(span)

    def stop(self, span: Span) -> bool:
        spans = _spans()
        span.finish(self.segment)
        del spans[spans.index(span)]

        self._nspans -= 1
        if self._nspans == 0:
            _local().context = None
            agent.archive(self.segment)
            return True

        return False

    def active_span(self):
        spans = _spans()
        if spans:
            return spans[len(spans) - 1]

        return None

    def get_correlation(self, key):
        if key in self._correlation:
            return self._correlation[key]
        return None

    def put_correlation(self, key, value):
        if key is None:
            return
        if value is None:
            self._correlation.pop(key, value)
            return
        if len(value) > config.correlation_value_max_length:
            return
        if len(self._correlation) > config.correlation_element_max_number:
            return

        self._correlation[key] = value

    def capture(self):
        spans = _spans()
        if len(spans) == 0:
            return None

        return Snapshot(
            segment_id=str(self.segment.segment_id),
            span_id=self.active_span().sid,
            trace_id=self.segment.related_traces[0],
            endpoint=spans[0].op,
            correlation=self._correlation,
        )

    def continued(self, snapshot: "Snapshot"):
        if snapshot is None:
            return None
        if not snapshot.is_from_current(self) and snapshot.is_valid():
            ref = SegmentRef.build_ref(snapshot)
            span = self.active_span()
            span.refs.append(ref)
            self.segment.relate(ID(ref.trace_id))
            self._correlation.update(snapshot.correlation)


class NoopContext(SpanContext):
    def __init__(self):
        super().__init__()
        self._depth = 0
        self._noop_span = NoopSpan(self, kind=Kind.Local)
        self.correlation = {}  # type: dict

    def new_local_span(self, op: str) -> Span:
        return self._noop_span

    def new_entry_span(self, op: str, carrier: "Carrier" = None) -> Span:
        if carrier is not None:
            self._noop_span.extract(carrier)
        return self._noop_span

    def new_exit_span(self, op: str, peer: str) -> Span:
        return self._noop_span

    def start(self, span: Span):
        self._depth += 1

    def stop(self, span: Span) -> bool:
        self._depth -= 1
        return self._depth == 0

    def active_span(self):
        return self._noop_span

    def capture(self):
        return Snapshot(
            segment_id=None,
            span_id="",
            trace_id=None,
            endpoint=None,
            correlation=self._correlation,
        )

    def continued(self, snapshot: "Snapshot"):
        self._correlation.update(snapshot.correlation)


def get_context() -> SpanContext:
    local = _local()
    context = getattr(local, "context", False)

    if not context:
        context = local.context = SpanContext() if agent.connected() else NoopContext()
        _spans_set([])  # XXX would be better in SpanContext.__init__() but for some reason doesn't work there

    return context
