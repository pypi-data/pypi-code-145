# This file is autogenerated by the command `make fix-copies`, do not edit.
# flake8: noqa

from ..utils import DummyObject, requires_backends


class PunctuationRestorer(metaclass=DummyObject):
    _backends = ["transformers"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["transformers"])

    @classmethod
    def from_config(cls, *args, **kwargs):
        requires_backends(cls, ["transformers"])

    @classmethod
    def from_pretrained(cls, *args, **kwargs):
        requires_backends(cls, ["transformers"])
