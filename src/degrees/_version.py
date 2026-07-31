"""The version info of the degree package."""
from typing import Literal as _Literal, NamedTuple as _NamedTuple

__all__: list[str] = ['version_info']

_Releaselevel = _Literal['alpha', 'beta', 'candidate', 'final', 'post']

# noinspection PyPep8Naming
class version_info(_NamedTuple):  # type: ignore
    """The version info of the degree package."""
    major: int
    minor: int
    micro: int
    releaselevel: _Releaselevel = 'final'
    serial: int = 0

    def __repr__(self):
        return f'degrees.version_info(major={self.major}, minor={self.minor}, micro={self.micro}, releaselevel={self.releaselevel!r}, serial={self.serial})'

version_info: _NamedTuple = version_info(0, 5, 1)  # type: ignore
