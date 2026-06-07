"""The version info of the degree package."""
from typing import Literal as _Literal, NamedTuple as _NamedTuple

__all__: list[str] = ['version_info']

_Releaselevel = _Literal['alpha', 'beta', 'candidate', 'final', 'post']

# noinspection PyPep8Naming
class version_info(_NamedTuple):
    """The version info of the degree package."""
    major: int
    minor: int
    micro: int
    releaselevel: _Releaselevel = 'final'
    serial: int = 0

    def __repr__(self):
        return f'version_info({self.major}, {self.minor}, {self.micro}, {self.releaselevel!r}, {self.serial})'

version_info = version_info(0, 4, 0)
