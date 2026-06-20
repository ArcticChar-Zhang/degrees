from ._degrees import Degree as _Degree, _assert  # type: ignore
from collections.abc import Callable

to_gon: Callable[[_Degree], float] = lambda x: _assert(x, _Degree).total_seconds / 3240
to_gon.__doc__ = ''
to_turn: Callable[[_Degree], float] = lambda x: _assert(x, _Degree).total_seconds / 1296000
from_gon: Callable[[int | float], _Degree] = lambda x: _Degree(second=int(_assert(x, int | float) * 3240))
from_turn: Callable[[int | float], _Degree] = lambda x: _Degree(second=int(_assert(x, int | float) * 1296000))
