import copy
import ctypes

import torch


# credit
# https://github.com/pyro-ppl/pyro/blob/beddc1f1a193d7f03bd588c9d6afe389bbd2d10c/pyro/distributions/util.py
class _DeepToMemo(dict):
    def __init__(self, to_args, to_kwargs):
        super().__init__()
        self._to_args = to_args
        self._to_kwargs = to_kwargs

    def get(self, key, default=None):
        result = super().get(key, default)
        if result is default:
            # Assume key is the id of another object, and look up that object.
            old = ctypes.cast(key, ctypes.py_object).value
            if isinstance(
                old, (torch.Tensor, torch.nn.Module)
            ):  # or maybe duck type here?
                self[key] = result = old.to(*self._to_args, **self._to_kwargs)
        return result


def deep_to(obj, *args, **kwargs):
    memo = _DeepToMemo(args, kwargs)
    return copy.deepcopy(obj, memo)
