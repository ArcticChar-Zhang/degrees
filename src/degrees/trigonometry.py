"""Trigonometric functions for Degree objects."""
from ._degrees import Degree, degree2radian as _d2r, radian2degree as _r2d
import math as _math
from collections.abc import Callable

__all__ = ['sin', 'cos', 'tan', 'cot', 'sec', 'csc',
           'asin', 'acos', 'atan', 'acot', 'asec', 'acsc']

sin: Callable[[Degree], float] = lambda x: _math.sin(_d2r(x))
cos: Callable[[Degree], float] = lambda x: _math.cos(_d2r(x))
tan: Callable[[Degree], float] = lambda x: _math.tan(_d2r(x))
cot: Callable[[Degree], float] = lambda x: 1 / tan(x)
sec: Callable[[Degree], float] = lambda x: 1 / cos(x)
csc: Callable[[Degree], float] = lambda x: 1 / sin(x)

asin: Callable[[int | float], Degree] = lambda x: _r2d(_math.asin(x))
acos: Callable[[int | float], Degree] = lambda x: _r2d(_math.acos(x))
atan: Callable[[int | float], Degree] = lambda x: _r2d(_math.atan(x))
acot: Callable[[int | float], Degree] = lambda x: _r2d(_math.atan(1 / x))
asec: Callable[[int | float], Degree] = lambda x: _r2d(_math.acos(1 / x))
acsc: Callable[[int | float], Degree] = lambda x: _r2d(_math.asin(1 / x))

del Callable
