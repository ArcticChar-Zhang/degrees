"""A python library for degree calculations and conversions."""
from ._degrees import *
from ._version import *
from . import trigonometry
from ._consts import *

__all__: list[str] = [
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
    'GOLDEN_ANGLE'
]

__author__ = 'Zhang Jiarui'


def set_north(n: int | float | Degree, /):
    """Set north to n, east to (n + 90), south to (n + 180), west to (n + 270).
    Never Use \"NORTH=Degree(xxx)\"."""
    global NORTH, EAST, SOUTH, WEST
    NORTH = Degree(n)  # type: ignore
    EAST = normalize(NORTH + 90)  # type: ignore
    SOUTH = normalize(NORTH + 180)  # type: ignore
    WEST = normalize(NORTH + 270)  # type: ignore
