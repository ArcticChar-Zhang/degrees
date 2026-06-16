"""A python library for degree calculations and conversions."""
from ._degrees import (Degree,
                       degree2radian,
                       radian2degree,
                       normalize,
                       DEGREE,
                       MINUTE,
                       SECOND)
from ._version import version_info
from . import trigonometry

__all__: list[str] = [
    'Degree',
    'degree2radian',
    'radian2degree',
    'normalize',
    'version_info',
    'DEGREE',
    'MINUTE',
    'SECOND',
    'trigonometry'
]

__author__ = 'Zhang Jiarui'
