from ._degrees import Degree as _Deg

__all__ = ['RIGHT_ANGLE', 'STRAIGHT_ANGLE', 'FULL_ANGLE', 'ZERO_ANGLE',
           'HALF_PI', 'PI', 'TWO_PI',
           'NORTH', 'EAST', 'SOUTH', 'WEST',
           'THIRTY_DEG', 'FORTY_FIVE_DEG', 'SIXTY_DEG', 'GOLDEN_ANGLE']

RIGHT_ANGLE = HALF_PI = EAST = _Deg(90)
STRAIGHT_ANGLE = PI = SOUTH = _Deg(180)
FULL_ANGLE = TWO_PI = _Deg(360)
WEST = _Deg(270)
ZERO_ANGLE = NORTH = _Deg()

THIRTY_DEG = _Deg(30)
FORTY_FIVE_DEG = _Deg(45)
SIXTY_DEG = _Deg(60)

GOLDEN_ANGLE = _Deg(137.50776405003785)

del _Deg
