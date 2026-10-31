# noinspection PyProtectedMember
from ._degrees import Degree as _D, NormalizedDegree as _ND, _assert  # type: ignore
from collections.abc import Callable
from typing import Any

__all__ = ['is_']
_norm: Callable[[Any], _ND] = lambda x: _ND(_assert(x, _D))

class _Is:
    """Judgements for types of Degree instances.
    All Judgements except for is_.round supports both Degree and NormalizedDegree,
    but is_.round only supports Degree objects."""
    acute: Callable[[Any, _D], bool] = lambda _, x: 0 < _norm(x) < 90
    right: Callable[[Any, _D], bool] = lambda _, x: _norm(x) == 90
    obtuse: Callable[[Any, _D], bool] = lambda _, x: 90 < _norm(x) < 180
    straight: Callable[[Any, _D], bool] = lambda _, x: _norm(x) == 180
    major: Callable[[Any, _D], bool] = lambda _, x: 180 < _norm(x) < 360
    minor: Callable[[Any, _D], bool] = lambda _, x: 0 < _norm(x) < 180
    zero: Callable[[Any, _D], bool] = lambda _, x: _assert(x, _D) == 0
    round: Callable[[Any, _D], bool] = \
        lambda _, x: _assert(x, _D) % _D(360) == 0 and \
        x != 0  # does not support NormalizedDegree

is_ = _Is()
del Any, Callable, _Is
