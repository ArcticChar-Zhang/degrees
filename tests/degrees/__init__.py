"""A python library for degree calculations and conversions."""
from ._degrees import *
from ._version import *
from . import trigonometry
from ._consts import *
from ._exchanges import *
from ._judgements import *
from warnings import warn as _warn
from contextlib import contextmanager as _con
from collections.abc import Generator
from typing import Any

__all__: list[str] = [
    '__author__',
    'Degree',
    'degree2radian',
    'radian2degree',
    'normalize',
    'version_info',
    'DEGREE',
    'MINUTE',
    'SECOND',
    'trigonometry',
    'RIGHT_ANGLE',
    'STRAIGHT_ANGLE',
    'FULL_ANGLE',
    'ZERO_ANGLE',
    'HALF_PI',
    'PI',
    'TWO_PI',
    'NORTH',
    'EAST',
    'SOUTH',
    'WEST',
    'THIRTY_DEG',
    'FORTY_FIVE_DEG',
    'SIXTY_DEG',
    'GOLDEN_ANGLE',
    'set_north',
    'arg',  # 0.5.1+
    'safe_set_north',
    'to_gon',
    'to_turn',
    'from_gon',
    'from_turn',
    'NormalizedDegree',  # 0.6.0+
    'is_',  # 0.6.1+
    'north',  # 0.6.3+
    'east',  # 0.6.3+
    'south',  # 0.6.3+
    'west'  # 0.6.3+
]

__author__ = 'Zhang Jiarui'


def set_north(n: int | float | Degree, /, warn: bool = True) -> None:
    """Set north to n, east to (n + 90), south to (n + 180), west to (n + 270).
    Never Use \"north=Degree(xxx)\".
    WARNING: Set global cardinal directions. NOT thread-safe. For single-threaded use only."""
    if warn is not True and warn is not False:
        raise TypeError('argument "warn" must be True or False')
    if warn:
        _warn('Set global cardinal directions. NOT thread-safe. For single-threaded use only.',
              RuntimeWarning)
    global north, east, south, west
    north = Degree(n)
    east = normalize(north + 90)
    south = normalize(north + 180)
    west = normalize(north + 270)

@_con
def safe_set_north(n: int | float | Degree, /) -> Generator[None, Any, None]:
    """Set north to n, east to (n + 90), south to (n + 180), west to (n + 270).
    Never Use \"north=Degree(xxx)\".
    This function is thread-safe and guarantees state restoration via context manager."""
    # noinspection PyGlobalUndefined
    global north, east, south, west
    north = Degree(n)
    east = normalize(north + 90)
    south = normalize(north + 180)
    west = normalize(north + 270)
    try:
        yield
    finally:
        north, east, south, west = \
        NORTH, EAST, SOUTH, WEST

del _con, Generator, Any
