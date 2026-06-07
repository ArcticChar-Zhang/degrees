"""A python library for degree calculations and conversions."""
import sys
from math import (radians as _radians,
                  degrees as _degrees,
                  cos as _cos,
                  sin as _sin)
from sys import version_info as _version_info
from collections.abc import Iterable, Callable
from inspect import currentframe as _currentframe
from warnings import warn as _warn

__all__: list[str] = [
    "Degree",
    "degree2radian",
    "radian2degree",
    "normalize",
    "DEGREE",
    "MINUTE",
    "SECOND"
]

DEGREE = '\u00b0'
MINUTE = '\u2032'
SECOND = '\u2033'

if _version_info >= (3, 11):
    from typing import Any, overload, Self
else:
    from typing import Any, overload, TypeVar  # pragma: no cover
    Self = TypeVar("Self", bound="Degree")  # pragma: no cover


class _Type:
    num_or_deg = int | float | Self
    builtin_real_number = int | float

class Degree:
    __slots__ = ('total_seconds', '_s', '_d', '_m', '_si')

    @overload
    def __init__(self, degree: int = 0, minute: int = 0, second: int = 0) -> None: ...
    @overload
    def __init__(self, number: float) -> None: ...
    @overload
    def __init__(self, degree_obj: Self) -> None: ...
    def __init__(self, degree: _Type.num_or_deg = 0,
                 minute: int = 0,
                 second: int = 0) -> None:
        """Create a degree object"""
        self.total_seconds: int
        if not isinstance(degree, (int, float, Degree)):
            raise TypeError("invalid type")
        if degree == 0 and minute == 0:
            if not isinstance(second, int) or not isinstance(minute, int):
                raise TypeError("invalid type")
            self.total_seconds = second
            return
        if isinstance(degree, float):
            if second != 0 or minute != 0 or not isinstance(second, int) or not isinstance(minute, int):
                raise TypeError("if the type of degree is float, second and minute must be 0")
            self.total_seconds = int(degree * 3600)
            return
        if isinstance(degree, Degree):
            if minute != 0 or second != 0 or not isinstance(second, int) or not isinstance(minute, int):
                raise ValueError("if the type of degree is Degree, minute and second must be 0")
            self.total_seconds = degree.total_seconds
            return
        if isinstance(degree, int):
            if (degree != 0 and (minute < 0 or second < 0)) or not isinstance(second, int) or not\
                    isinstance(minute, int):
                raise ValueError("if degree is not 0, minute and second must be positive integer")
            self.total_seconds = abs(degree) * 3600 + abs(minute) * 60 + abs(second)
            if degree < 0 or minute < 0 or second < 0:
                self.total_seconds = -self.total_seconds
            if minute != 0 and second < 0:
                raise ValueError("if degree is 0, but minute is not, second must be positive integer")

        if not isinstance(self.total_seconds, int):
            raise TypeError("unknown type")  # pragma: no cover

    def __abs__(self) -> Self:
        """Return the absolute value of the degree object"""
        return Degree(second=self.total_seconds)

    def __str__(self) -> str:
        r: str = "" if self.total_seconds > 0 else "-"
        if self.total_seconds == 0:
            return f"0{DEGREE}"
        if self.deg != 0 and self.sec != 0:
            return r + f"{self.deg}{DEGREE}{self.min}{MINUTE}{self.sec}{SECOND}"
        if self.deg != 0:
            r += f"{self.deg}{DEGREE}"
        if self.min != 0:
            r += f"{self.min}{MINUTE}"
        if self.sec != 0:
            r += f'{self.sec}{SECOND}'
        return r

    __str__.__doc__ = \
        f"""Return the string form of the degree object
    Examples:
        Degree(1) -> 1{DEGREE}
        Degree(1, 3, 5) -> 1{DEGREE}3{MINUTE}5{SECOND}
        Degree(1, 0, 5) -> 1{DEGREE}0{MINUTE}5{SECOND}
        Degree(1, 3) -> 1{DEGREE}3{MINUTE}
        ..."""

    def __repr__(self) -> str:
        """return the repr form of the degree object"""
        return "Degree" + str(self.dms)

    def __pos__(self) -> Self:
        """Return self unchanged"""
        return self

    def __neg__(self) -> Self:
        """Return self negated"""
        return Degree(second=-self.total_seconds)

    def __ceil__(self) -> int:
        """Return the least Integral >= x"""
        if self < Degree(0):
            return int(self)
        if self == Degree(0):
            return 0
        if not (self.min or self.sec):
            return self.deg
        return self.deg + 1

    def __floor__(self) -> int:
        """Return the greatest Integral <= x"""
        if self > Degree(0):
            return int(self)
        if self == Degree(0):
            return 0
        if not (self.min or self.sec):
            return -self.deg
        return -self.deg - 1

    def __int__(self) -> int:
        """Return the integer form of the degree object"""
        return self.deg * self.sign

    def __float__(self) -> float:
        """Return the float form of the degree object"""
        number = self.total_seconds / 3600
        return float(int(number * 1000) / 1000)

    def __bool__(self) -> bool:
        """Return True if the degree object is not equal to zero, else false"""
        return self != Degree(0)

    def __eq__(self, other: Any) -> bool:
        """Return self is equal to other"""
        if isinstance(other, int):
            return self.total_seconds == other * 3600
        if isinstance(other, Degree):
            return self.total_seconds == other.total_seconds
        return float(self) == other

    def __gt__(self, other: _Type.num_or_deg) -> bool:
        """Return self is strictly greater than other"""
        if isinstance(other, Degree):
            return self.total_seconds > other.total_seconds
        if isinstance(other, int):
            return self.total_seconds > other * 3600
        if isinstance(other, float):
            return float(self) > other
        raise TypeError("invalid type")

    def __lt__(self, other: _Type.num_or_deg) -> bool:
        """Return self is strictly less than other"""
        return not self >= other

    def __ge__(self, other: _Type.num_or_deg) -> bool:
        """Return self is greater than or equal to other"""
        return self > other or self == other

    def __le__(self, other: _Type.num_or_deg) -> bool:
        """Return self is less than or equal to other"""
        return not self > other

    def __ne__(self, other: Any) -> bool:
        """Return self is not equal to other"""
        return not self == other

    def __add__(self, other: _Type.num_or_deg) -> Self:
        """Return the sum of self and other"""
        oth: Degree = Degree(other)
        ttsec: int = self.total_seconds + oth.total_seconds
        return Degree(second=ttsec)

    def __radd__(self, other: _Type.num_or_deg) -> Self:
        """Return the sum of other and self"""
        return self + other

    def __sub__(self, other: _Type.num_or_deg) -> Self:
        """Return the difference of self and other"""
        return self + -other

    def __rsub__(self, other: _Type.num_or_deg) -> Self:
        """Return the difference of other and self"""
        return -(self.__sub__(other))

    def __mul__(self, other: _Type.num_or_deg) -> Self:
        """Return the product of self and other"""
        if isinstance(other, Degree):
            _warn('"Degree_obj" * "Degree_obj" is deprecated since version 0.4.0, will be removed in version 0.5'
                  '.0.', DeprecationWarning)
            srad = degree2radian(self)
            orad = degree2radian(other)
            resrad = srad * orad
            resdeg = _degrees(resrad)
            return Degree(resdeg)
        if isinstance(other, (int, float)):
            tts = int(self.total_seconds * other)
            return Degree(second=tts)
        raise Exception("invalid type")

    def __rmul__(self, other: _Type.num_or_deg) -> Self:
        """Return the product of other and self"""
        return self * other

    @overload
    def __truediv__(self, other: Self) -> float: ...
    @overload
    def __truediv__(self, other: _Type.builtin_real_number) -> Self: ...
    def __truediv__(self, other: _Type.num_or_deg) -> Self | float:
        """Return the quotient of self and other"""
        if other == 0:
            raise ZeroDivisionError("division by zero")
        if isinstance(other, (int, float)):
            tts = self.total_seconds // other
            return Degree(second=tts)
        sts = self.total_seconds
        ots = other.total_seconds
        return sts / ots

    @overload
    def __floordiv__(self, other: Self) -> float: ...
    @overload
    def __floordiv__(self, other: _Type.builtin_real_number) -> Self: ...
    def __floordiv__(self, other: _Type.num_or_deg) -> Self | int:
        """Return the floored quotient of self and other"""
        if other == 0:
            raise ZeroDivisionError("division by zero")
        if isinstance(other, (int, float)):
            res = self.deg * self.sign // other
            return Degree(res)
        sts = self.total_seconds
        ots = other.total_seconds
        return sts // ots

    def __mod__(self, other: Self) -> Self:
        """Return the remainder of 'self / other'"""
        if other == Degree(0):
            raise ZeroDivisionError("modulo by zero")
        sts = self.total_seconds
        ots = other.total_seconds
        # noinspection PyTypeChecker
        return Degree(second=sts % ots)  # type: ignore

    def __hash__(self) -> int:
        """Return the hash value of the degree object"""
        return hash((self.deg, self.min, self.sec, self.sign))

    def __setattr__(self, key, value) -> None:
        frame = _currentframe()
        if frame is None:
            del frame  # pragma: no cover
            import sys as _sys  # pragma: no cover
            if not hasattr(_sys, '_getframe'):  # pragma: no cover
                raise AttributeError("read-only attribute")  # pragma: no cover
            frame = sys._getframe()  # pragma: no cover
        if frame.f_back.f_code.co_filename != __file__:
            del frame
            raise AttributeError("read-only attribute")
        del frame
        super().__setattr__(key, value)

    __trunc__ = __int__

    @classmethod
    def _construct(cls, tts: int) -> object:
        obj = cls.__new__(cls)
        object.__setattr__(obj, 'total_seconds', tts)
        return obj

    def __reduce_ex__(self, protocol: int) -> \
            tuple[Callable[[int], object], tuple[int]]:
        return (
            self._construct,
            (self.total_seconds,)
        )

    @property
    def deg(self) -> int:
        """Return the total number of seconds"""
        if not hasattr(self, '_d'):
            setattr(self, '_d', abs(self.total_seconds) // 3600)
        return getattr(self, '_d')

    @property
    def min(self) -> int:
        """Return the total number of seconds"""
        if not hasattr(self, '_m'):
            setattr(self, '_m', abs(self.total_seconds) % 3600 // 60)
        return getattr(self, '_m')

    @property
    def sec(self) -> int:
        """Return the total number of seconds"""
        if not hasattr(self, '_s'):
            setattr(self, '_s', abs(self.total_seconds) % 60)
        return getattr(self, '_s')

    @property
    def sign(self) -> int:
        """Return the sign of the degree"""
        if not hasattr(self, '_si'):
            _ = self.total_seconds
            if _ > 0:
                a = 1
            elif _ < 0:
                a = -1
            else:
                a = 0
            setattr(self, '_si', a)
        return getattr(self, '_si')

    @staticmethod
    def from_str(string: str) -> Self:
        """Create a degree from a string"""
        if string.isdecimal():
            return Degree(int(string))
        charset = ''
        signs = (DEGREE, "'", '"')
        if string[-1] not in signs:
            raise ValueError("Incorrect string format")
        set_ = ()
        for i in string:
            if i.isdigit():
                charset += str(i)
            else:
                set_ += ((int(charset), signs.index(i)),)
                charset = ''
        if len(set_) > 3:
            raise ValueError("Incorrect string format")
        # noinspection PyTypeChecker
        if set_[0][1] == 0 and set_[1][1] == 2:  # type: ignore
            raise ValueError(f'Incorrect string format: do not support strings like "a{DEGREE}b{SECOND}", '
                             f'please use "a{DEGREE}0{MINUTE}b{SECOND}".')
        deg = min_ = sec = 0
        judge = -1
        for i in set_:
            # noinspection PyUnresolvedReferences
            if i[1] <= judge:  # type: ignore
                raise ValueError("Incorrect string format")  # type: ignore
            # noinspection PyUnresolvedReferences
            judge = i[1]
            # noinspection PyUnresolvedReferences
            if judge == 0:  # type: ignore
                # noinspection PyUnresolvedReferences
                deg = i[0]  # type: ignore
            elif judge == 1:  # type: ignore
                # noinspection PyUnresolvedReferences
                min_ = i[0]  # type: ignore
            else:
                # noinspection PyUnresolvedReferences
                sec = i[0]  # type: ignore
        return Degree(deg, min_, sec)

    @staticmethod
    def from_unicode(string: str) -> Self:
        """Create a degree from a string"""
        if string.isdecimal():
            return Degree(int(string))
        charset = ''
        signs = (DEGREE, MINUTE, SECOND)
        if string[-1] not in signs:
            raise ValueError("Incorrect unicode string format")
        set_ = ()
        for i in string:
            if i.isdigit():
                charset += str(i)
            else:
                set_ += ((int(charset), signs.index(i)),)
                charset = ''
        if len(set_) > 3:
            raise ValueError("Incorrect unicode string format")
        # noinspection PyTypeChecker
        if set_[0][1] == 0 and set_[1][1] == 2:  # type: ignore
            raise ValueError(f'Incorrect string format: do not support strings like "a{DEGREE}b{SECOND}", '
                             f'please use "a{DEGREE}0{MINUTE}b{SECOND}".')
        deg = min_ = sec = 0
        judge = -1
        for i in set_:
            # noinspection PyUnresolvedReferences
            if i[1] <= judge:  # type: ignore
                raise ValueError("Incorrect string format")  # type: ignore
            # noinspection PyUnresolvedReferences
            judge = i[1]
            # noinspection PyUnresolvedReferences
            if judge == 0:  # type: ignore
                # noinspection PyUnresolvedReferences
                deg = i[0]  # type: ignore
            elif judge == 1:  # type: ignore
                # noinspection PyUnresolvedReferences
                min_ = i[0]  # type: ignore
            else:
                # noinspection PyUnresolvedReferences
                sec = i[0]  # type: ignore
        return Degree(deg, min_, sec)

    @staticmethod
    def from_iter(iterable: Iterable[int]) -> Self:
        """Return a degree object from an iterable
        Accept forms:
        1) (deg, min, sec)
        2) (deg, min, sec, sign)
        Note(for iterable with 4 items):
        if sign is greater than 0, return a positive degree object
        if sign is 0, return Degree(0). if sign is 0, the iterable must be (0, 0, 0, 0)
        if sign is less than 0, return a negative degree object"""
        # noinspection PyTypeChecker
        iter_ = tuple(iterable)  # type: ignore
        if len(iter_) == 3:
            return Degree(*iter_)
        elif len(iter_) == 4:
            if (iter_[0] != 0 or iter_[1] != 0 or iter_[2] != 0) and iter_[3] == 0:
                raise ValueError("Incorrect iter format.You can see the doc:\n" + Degree.from_iter.__doc__)
            _ = 1 if (iter_[3] > 0) else -1
            return Degree(*iter_[:3]) * _
        raise ValueError("Incorrect iter format")

    @property
    def dms(self) -> tuple[int, int, int]:
        d, m, s = self.deg, self.min, self.sec
        if self.sign == -1:
            if d > 0:
                d = -d
            elif m > 0:
                m = -m
            elif s > 0:
                s = -s
        return d, m, s

    def to_complex(self, length: _Type.builtin_real_number) -> complex:
        if length < 0:
            raise ValueError("length must be non-negative")
        theta = degree2radian(self)
        return complex(
            length * _cos(theta),
            length * _sin(theta)
        )

def degree2radian(x: Degree, /) -> float:
    """Convert angle x from a degree object to radians"""
    return _radians(x.total_seconds / 3600)

def radian2degree(x: _Type.builtin_real_number, /) -> Degree:
    """Convert angle x from radians to a degree object"""
    return Degree(_degrees(x))

def normalize(x: Degree, /) -> Degree:
    """Be using for angle normalization"""
    tts = x.total_seconds * x.sign
    norms = tts % 1_296_000
    return Degree(second=norms)

del Any, overload, Self, Iterable, _Type
if _version_info < (3, 11):
    del TypeVar  # pragma: no cover
