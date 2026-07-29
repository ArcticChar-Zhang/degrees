"""This submodule can be used for exchanging to/from gon/turn."""
# noinspection PyProtectedMember
from ._degrees import Degree as _Degree, _assert  # type: ignore
from collections.abc import Callable

to_gon: Callable[[_Degree], float] = lambda x: _assert(x, _Degree).total_seconds / 3240
to_turn: Callable[[_Degree], float] = lambda x: _assert(x, _Degree).total_seconds / 1296000
from_gon: Callable[[int | float], _Degree] = lambda x: _Degree(second=int(_assert(x, int | float) * 3240))
from_turn: Callable[[int | float], _Degree] = lambda x: _Degree(second=int(_assert(x, int | float) * 1296000))

to_gon.__doc__ = 'Convert angle x from a degree object to gon.'
to_turn.__doc__ = 'Convert angle x from a degree object to turn.'
from_gon.__doc__ = 'Convert angle x from gon to a degree object.'
from_turn.__doc__ = 'Convert angle x from turn to a degree object.'

del Callable
