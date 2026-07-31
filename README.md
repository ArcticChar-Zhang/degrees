# degrees V0.5.1
# Back to PyPI: click [here](https://pypi.org/project/degrees/)
# Contents
* [Introduction](#introduction)
* [Installing](#installing)
* [Importing](#importing)
* [Class](#class)
  * [Degree](#class-degreesdegreenumberclass-degreesdegreedegree_objclass-degreesdegreedegree0-minute0-second0)
* [Functions](#functions)
  * [Functions for converting](#functions-for-converting)
  * [normalize](#degreesnormalizex-degree--origin-int--float--degree--0)
  * [arg](#degreesargx-complex)
  * [set_north](#degreesset_northn-degree--int--float--warn-bool--true)
  * [safe_set_north](#contextmanager-degreessafe_set_northn-degree--int--float-)
* [Constants](#constants)
  * [DEGREE<br>MINUTE<br>SECOND](#degreesdegreedegreesminutedegreessecond)
  * [\_\_author\_\_](#degrees__author__)
* [Submodule](#submodule)
* [Changelog](#changelog)
* [Older versions](#older-versions)
# Introduction
### A Python library for degree calculations and conversions.
> [!TIP]
> ### **Added in version 0.2:** Supported `pickle`.

> [!WARNING]
> ### Changed all the attributes of _class_ `Degree` to properties in version `0.4.3`. You need to be careful if you use `pickle`.

> [!NOTE]
> ### If you want to see the code of this module, please look at the code in `src` folder; the `tests` folder is for developing, if you want to see the progress of developing or help me develop, please look at the code in `src` folder.
# Installing
| Python version |                   Windows                    |            macOS / Linux            |
|:--------------:|:--------------------------------------------:|:-----------------------------------:|
| `3.8` or `3.9` | `python -m pip install degrees==0.3.0.post1` | `pip3 install degrees==0.3.0.post1` |
|    `3.10+`     |       `python -m pip install degrees`        |       `pip3 install degrees`        |

If you use `python 3.8` or `3.9`, please read [the docs here](https://pypi.org/project/degrees/0.3.0.post1/).
# Importing
### Just type `import degrees`.
//# Class
- ## _class degrees_.Degree(number)<br>_class degrees_.Degree(degree_obj)<br>_class degrees_.Degree(degree=0, minute=0, second=0)
   Degree main class.
   > [!NOTE]
   > Calculation results based on Degree object may be truncated.

   - ### Creating a Degree object

   > [!WARNING]
   > **Changed in version 0.4.2:** The arguments' names are changed since version 0.4.2. Please be careful if you
   > use keyword arguments. Now the arguments are: `degree`, `minute`, `second`. It does not depend on the overloads.
```python 
import degrees

print(degrees.Degree(1))  # 1°
print(degrees.Degree(2, 3, 4))  # 2°3′4″
print(degrees.Degree(1, second=2))  # 1°0′2″
print(degrees.Degree(1, 3))  # 1°3′
print(degrees.Degree(0, -1))  # -1′
print(degrees.Degree(1.5))  # 1°30′
print(degrees.Degree(2, -4))  # ValueError: if degree is not 0, minute and second must be positive integer
```

   - ### calculating:
   |   expressions   |   `type(a)`    |     `type(b)`      | return type |
   |:---------------:|:--------------:|:------------------:|:-----------:|
   |     `a + b`     |    `Degree`    |   `int \| float`   |  `Degree`   |
   |                 | `int \| float` |      `Degree`      |  `Degree`   |
   |     `a - b`     |    `Degree`    |   `int \| float`   |  `Degree`   |
   |                 | `int \| float` |      `Degree`      |  `Degree`   |
   |     `a * b`     |    `Degree`    |   `int \| float`   |  `Degree`   |
   |                 | `int \| float` |      `Degree`      |  `Degree`   |
   |     `a / b`     |    `Degree`    |      `Degree`      |   `float`   |
   |                 |    `Degree`    |   `int \| float`   |  `Degree`   |
   | `math.trunc(a)` |    `Degree`    |         /          |  `Degree`   |
   |   `round(a)`    |    `Degree`    |         /          |    `int`    |
   |  `round(a, b)`  |    `Degree`    | `Literal[1, 2, 3]` |    `int`    |
   |    `abs(a)`     |    `Degree`    |         /          |  `Degree`   |
   | `math.ceil(a)`  |    `Degree`    |         /          |  `Degree`   |
   | `math.floor(a)` |    `Degree`    |         /          |  `Degree`   |
   |     `a % b`     |    `Degree`    |      `Degree`      |  `Degree`   |
   |    `a // b`     |    `Degree`    |      `Degree`      |    `int`    |
   |                 |    `Degree`    |   `int \| float`   |  `Degree`   |
   |      `+a`       |    `Degree`    |         /          |  `Degree`   |
   |      `-a`       |    `Degree`    |         /          |  `Degree`   |
   |    `hash(a)`    |    `Degree`    |         /          |    `int`    |
   
   > [!NOTE]
   > The `round` function's usage:<br>
   > &#9;Return the nearest integer to its input if `ndigits` is omitted or None.<br>
   > &#9;Return self rounded to nearest degree if `ndigits` is 1.<br>
   > &#9;Return self rounded to nearest minute if `ndigits` is 2.<br>
   > &#9;Return self not changed if `ndigits` is 3.<br>
   > &#9;Otherwise, raise ValueError.<br>
   > (`ndigits`/`b` is the second argument.)

   > [!TIP]
   > **Added in version 0.1.7:** Implemented the `math.trunc` function on the Degree objects.
    
   > [!TIP]
   > **Added in version 0.4.0:** Now `deg_obj * float_obj` is supported. In the previous version, only
`deg_obj * int_obj` is supported.
   
   > [!TIP]
   > **Added in version 0.5.1:** Added the `__round__` method.

   - ### conversions:
   | `int(a)` | `float(a)` | `str(a)` | `repr(a)` | `bool(a)` | `complex(a)` |
   |:--------:|:----------:|:--------:|:---------:|:---------:|:------------:|
    
   In the table above, `type(a)` is `Degree`.

   > [!IMPORTANT]
   > The `complex(degree_obj)` is different from `degree_obj.to_complex(r)`. The former returns
   > `int(degree_obj)+0j`, but the latter returns `complex(r * cos(theta), r * sin(theta))`,
   `theta=degree2radian(degree_obj)`.

   > [!WARNING]
   > **Changed in version 0.4.3:** `float(degree_obj)` now returns a precise value, but in the previous version, it returns a rounded value(eqivalent to `round(float(degree_obj), 3)` now).

For example:
```python
import degrees
a = degrees.Degree(45)
print(complex(a))  # (45+0j)
print(a.to_complex(2 ** 0.5))  # about (1+1j)
```

   - ### comparisons:
     | expressions | `type(a)` |        `type(b)`         |
     |:-----------:|:---------:|:------------------------:|
     |  `a >= b`   | `Degree`  | `Degree \| int \| float` |
     |   `a > b`   | `Degree`  | `Degree \| int \| float` |
     |  `a == b`   | `Degree`  |          `Any`           |
     |  `a <= b`   | `Degree`  | `Degree \| int \| float` |
     |   `a < b`   | `Degree`  | `Degree \| int \| float` |
     |  `a != b`   | `Degree`  |          `Any`           |
    
     In the table above, the return value is `bool`, `type(a)` and `type(b)` can be swapped.

   - ### _property_ deg
     The degree of a degree object(without sign).
   - ### _property_ min
     The minute of a degree object(without sign).
   - ### _property_ sec
     The second of a degree object(without sign).
   - ### _property_ sign
     The sign of a degree object.
   - ### _property_ dms
     A tuple of `(degree, minute, second)`.
   - ### _property_ total_seconds
     The total seconds of a degree object.
   - ### _staticmethod_ from_iter(iterable)
     Return a degree object from an iterable.
   - ### _staticmethod_ from_str(string)
     Return a degree object from a string. The **dms** characters should be **`°`, `'` and `"`**.
   - ### _staticmethod_ from_unicode(string)
     Similar to `from_str`, but the **dms** characters should be **`°`, `′` and `″`**.
   > [!TIP]
   > **Added in version 0.1.10.**
   - ### as_integer_ratio()
     Return a tuple of `(numerator, denominator)` which is the integer ratio of the degree object.
     For example, `Degree(1, 30).as_integer_ratio()` returns `(3, 2)`.
   > [!TIP]
   > **Added in version 0.4.3.**
   - ### is_integer()
     Return `True` if the degree object is an integer, else `False`. For example, `Degree(1, 30).is_integer()` returns
     `False`, but `Degree(1).is_integer()` returns `True`.
   > [!TIP]
   > **Added in version 0.4.3.**
   - ### to_complex(r: int | float)
     Returns the complex number corresponding to `(angle=self, radius=r)`.
   > [!TIP]
   > **Added in version 0.2.1.**
   
   > [!NOTE]
   > The attributes of Degree are read-only.
# Functions
### Functions for converting
   |   functions   |   input type   |  return type   |
   |:-------------:|:--------------:|:--------------:|
   |   `to_rad`    |    `Degree`    | `int \| float` |
   |  `from_rad`   | `int \| float` |    `Degree`    |
   |   `to_gon`    |    `Degree`    | `int \| float` |
   |  `from_gon`   | `int \| float` |    `Degree`    |
   |   `to_turn`   |    `Degree`    | `int \| float` |
   |  `from_turn`  | `int \| float` |    `Degree`    |
   
## _degrees_.normalize(x: Degree, /, origin: int | float | Degree = 0)
   - Normalize angle x to range `[origin, origin + 360)`.
## _degrees_.arg(x: complex)
   - Return argument(a Degree object), also known as the phase angle, of a complex number.
## _degrees_.set_north(n: Degree | int | float, /, warn: bool = True)
   - Set north to n, east to (n + 90), south to (n + 180), west to (n + 270).
   Never Use \"NORTH=Degree(xxx)\".
   > [!WARNING]
   > **Changed in version 0.5.1:** This function now raises a `RuntimeWarning` because 
   > it is not thread-safe. You had better use the context manager `safe_set_north`.
## _contextmanager degrees_.safe_set_north(n: Degree | int | float, /)
   - The context manager version of function `set_north`.
   > [!TIP]
   > **Added in version 0.5.1.**
# Version
## version_info
   - The version of this package, like
[`sys.version_info`](https://docs.python.org/3.14/library/sys.html#sys.version_info).
   > [!NOTE]
   > `version_info[3]` or `version_info.releaselevel` may be `alpha`, `beta`, `candidate`, `final` or <u>`post`</u>.
# Constants
## _degrees_.DEGREE<br>_degrees_.MINUTE<br>_degrees_.SECOND
   Equals to `°`, `′` and `″`.
## some other consts
   |               name               |         value         |
   |:--------------------------------:|:---------------------:|
   |      `ZERO_ANGLE`, `NORTH`       |      `Degree(0)`      |
   |           `THIRTY_DEG`           |     `Degree(30)`      |
   |         `FORTY_FIVE_DEG`         |     `Degree(45)`      |
   |           `SIXTY_DEG`            |     `Degree(60)`      |
   | `RIGHT_ANGLE`, `HALF_PI`, `EAST` |     `Degree(90)`      |
   |          `GOLDEN_ANGLE`          | `Degree(137, 30, 27)` |
   | `STRAIGHT_ANGLE`, `PI`, `SOUTH`  |     `Degree(180)`     |
   |              `WEST`              |     `Degree(270)`     |
   |      `FULL_ANGLE`, `TWO_PI`      |     `Degree(360)`     |
   
   > [!NOTE]
   > You can use the function `set_north` and the context manager `safe_set_north` to set the constant `NORTH`,
   > then `EAST = (NORTH+90°) % 360°`, `SOUTH = (NORTH+180°) % 360°`, `WEST = (NORTH+270°) % 360°`.
   > Never use `degrees.NORTH = xxx` because `EAST`, `SOUTH` and `WEST` will **NOT** change.
   > [!TIP]
   > **Added the constants in the table above in version 0.5.0.**
## _degrees_.\_\_author\_\_
   The author of this package.
# Submodule
  - ## _module degrees_.trigonometry
     A submodule for trigonometric functions.
     Supported functions:

     | `sin` | `cos` | `tan` | `asin` | `acos` | `atan` |
     |:-----:|:-----:|:-----:|:------:|:------:|:------:|
     | `cot` | `sec` | `csc` | `acot` | `asec` | `acsc` |
     
     The functions start with `a` are inverse trigonometric functions, and the others are forward trigonometric
functions. Here is the input types and return types of these functions:<br>
     `def forward_trigonometric_function(x: Degree) -> float: ...`<br>
     `def inverse_trigonometric_function(x: int | float) -> Degree: ...`<br>
     (`forward_trigonometric_function` and `inverse_trigonometric_function` are referred to the functions in the table,
     and these two functions do not exist. Do not use them.)
# Changelog
   1. Added `Degree.__round__`.
   2. Added `arg`.
   3. Added `safe_set_north` and warn when `set_north` is called.
   4. Changed `Degree.__reduce_ex__` to `Degree.__reduce__`.
# Older versions
> Looking for src and a README older version?<br>
> Click [here](https://github.com/ArcticChar-Zhang/degrees/commits/main/) for V0.4.1+(include V0.4.1), next click the
> version you want, and then click "📄Browse files".<br>
> And [here](https://pypi.org/project/degrees/#history) for versions below V0.4.1.

> ### Write in the end
> If you found the bug in the code, you can email me at `snake830@vip.163.com`. I am happy to receive the advice!
