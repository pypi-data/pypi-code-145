from dataclasses import dataclass


@dataclass
class _UnlimiterBool:
    is_unlimiter_on: bool = False


_unlimiter = _UnlimiterBool(is_unlimiter_on=False)


def _turnUnlimiterOn() -> None:
    global _unlimiter
    _unlimiter.is_unlimiter_on = True


def IsUnlimiterOn() -> None:
    global _unlimiter
    return _unlimiter.is_unlimiter_on == True
