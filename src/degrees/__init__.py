"""A python library for degree calculations and conversions."""
from ._degrees import (Degree,
                       degree2radian,
                       radian2degree,
                       normalize,
                       DEGREE,
                       MINUTE,
                       SECOND)
from ._version import version_info

__all__: list[str] = [
    'Degree',
    'degree2radian',
    'radian2degree',
    'normalize',
    'version_info',
    'DEGREE',
    'MINUTE',
    'SECOND'
]

__author__ = 'Zhang Jiarui'
