# degrees V0.4.4
# Back to PyPI: click [here](https://pypi.org/project/degrees/)
# Contents
* [Introduction](#introduction)
* [Installing](#installing)
* [Importing](#importing)
* [Class](#class)
  * [Degree](#class-degreesdegreenumberclass-degreesdegreedegree_objclass-degreesdegreedegree0-minute0-second0)
* [Functions](#functions)
  * [degree2radian](#degreesdegree2radianx-degree-)
  * [radian2degree](#degreesradian2degreex-int--float-)
  * [normalize](#degreesnormalizex-degree-)
* [Consts](#consts)
  * [DEGREE<br>MINUTE<br>SECOND](#degreeminutesecond)
  * [\_\_author\_\_](#__author__)
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
| Python version | Windows                                      | macOS / Linux                       |
|----------------|----------------------------------------------|-------------------------------------|
| `3.8` or `3.9` | `python -m pip install degrees==0.3.0.post1` | `pip3 install degrees==0.3.0.post1` |
| `3.10+`        | `python -m pip install degrees`              | `pip3 install degrees`              |

If you use `python 3.8` or `3.9`, please read [the docs here](https://pypi.org/project/degrees/0.3.0.post1/).
# Importing
### Just type `import degrees`.
# Class
- ## _class degrees_.Degree(number)<br>_class degrees_.Degree(degree_obj)<br>_class degrees_.Degree(degree=0, minute=0, second=0)
   - ### Creating a Degree object
   > [!WARNING]
   > **Changed in version 0.4.0:** The arguments' names are changed since version 0.4.2. Please be careful if you
   > use keyword arguments. Now the arguments are: `degree`, `minute`, `second`. It does not depend on the overloads.
```python 
import degrees

print(degrees.Degree(1))  # 1°
print(degrees.Degree(2, 3, 4))  # 2°3'4"
print(degrees.Degree(1, second=2))  # 1°0'2"
print(degrees.Degree(1, 3))  # 1°3'
print(degrees.Degree(0, -1))  # -1'
print(degrees.Degree(1.5))  # 1°30'
print(degrees.Degree(2, -4))  # ValueError: if degree is not 0, minute and second must be positive integer
```

   - ### calculating:
    | expressions     | `type(a)`      | `type(b)`      | return type |
    |-----------------|----------------|----------------|-------------|
    | `a + b`         | `Degree`       | `int \| float` | `Degree`    |
    |                 | `int \| float` | `Degree`       | `Degree`    |
    | `a - b`         | `Degree`       | `int \| float` | `Degree`    |
    |                 | `int \| float` | `Degree`       | `Degree`    |
    | `a * b`         | `Degree`       | `int \| float` | `Degree`    |
    |                 | `int \| float` | `Degree`       | `Degree`    |
    |                 | `Degree`       | `Degree`       | `Degree`    |
    | `a / b`         | `Degree`       | `Degree`       | `float`     |
    |                 | `Degree`       | `int \| float` | `Degree`    |
    | `math.trunc(a)` | `Degree`       | /              | `Degree`    |
    | `abs(a)`        | `Degree`       | /              | `Degree`    |
    | `math.ceil(a)`  | `Degree`       | /              | `Degree`    |
    | `math.floor(a)` | `Degree`       | /              | `Degree`    |
    | `a % b`         | `Degree`       | `Degree`       | `Degree`    |
    | `a // b`        | `Degree`       | `Degree`       | `int`       |
    |                 | `Degree`       | `int \| float` | `Degree`    |
    | `+a`            | `Degree`       | /              | `Degree`    |
    | `-a`            | `Degree`       | /              | `Degree`    |
    | `hash(a)`       | `Degree`       | /              | `int`       |
   > [!TIP]
   > **Added in version 0.1.7:** Implemented the `math.trunc` function on the Degree objects.
    
   > [!TIP]
   > **Added in version 0.4.0:** Now `deg_obj * float_obj` is supported. In the previous version, only
`deg_obj * int_obj` is supported.
    
   > [!CAUTION]
   > **Deprecated since version 0.4.0, will be removed in version 0.5.0:** `Degree_obj * Degree_obj` is deprecated
because it is useless and strange.

   - ### conversions:
    | `int(a)` | `float(a)` | `str(a)` | `repr(a)` | `bool(a)` | `complex(a)` |
    |----------|------------|----------|-----------|-----------|--------------|
    
    In the table above, `type(a)` is `Degree`.

   > [!NOTE]
   > The `complex(degree_obj)` is different from `degree_obj.to_complex(r)`. The former returns
   > `int(degree_obj)+0j`, but the latter returns `complex(r * cos(theta), r * sin(theta))`,
   `theta=degree2radian(degree_obj)`.

   > [!WARNING]
   > **Changed in version 0.4.3:** `float(degree_obj)` now returnsa precise value, but in the previous version, it returns a rounded value(eqivalent to `round(float(degree_obj), 3)` now).

For example:
```python
import degrees
a = degrees.Degree(45)
print(complex(a))  # (45+0j)
print(a.to_complex(2 ** 0.5))  # about (1+1j)
```

   - ### comparisons:
     | expressions | `type(a)` | `type(b)`                |
     |-------------|-----------|--------------------------|
     | `a >= b`    | `Degree`  | `Degree \| int \| float` |
     | `a > b`     | `Degree`  | `Degree \| int \| float` |
     | `a == b`    | `Degree`  | `Any`                    |
     | `a <= b`    | `Degree`  | `Degree \| int \| float` |
     | `a < b`     | `Degree`  | `Degree \| int \| float` |
     | `a != b`    | `Degree`  | `Any`                    |
    
     In the table above, the return value is `bool`, `type(a)` and `type(b)` can be swapped.

   - ### _property_ deg
     The degree of a degree object(without sign).
   - ### _property_ dms
     A tuple of `(degree, minute, second)`.
   - ### _property_ min
     The minute of a degree object(without sign).
   - ### _property_ sec
     The second of a degree object(without sign).
   - ### _property_ sign
     The sign of a degree object.
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
     Return `True` if the degree object is an integer, else `False`. For example, `Degree(1, 30).is_integer()` returns `False`, but `Degree(1).is_integer()` returns `True`.
   > [!TIP]
   > **Added in version 0.4.3.**
   - ### to_complex(r: int | float)
     Returns the complex number corresponding to `(angle=self, radius=r)`.
   > [!TIP]
   > **Added in version 0.2.1.**
   
   > [!NOTE]
   > The attributes of Degree are read-only.
# Functions
## _degrees_.degree2radian(x: Degree, /)
   - Convert angle x from a degree object to radians.
## _degrees_.radian2degree(x: int | float, /)
   - Convert angle x from radians to a degree object.
## _degrees_.normalize(x: Degree, /)
   - Used for angle normalization.
# Version
## version_info
   - The version of this package, like
[`sys.version_info`](https://docs.python.org/3.14/library/sys.html#sys.version_info)
&larr; click for more info.
# Consts
## DEGREE<br>MINUTE<br>SECOND
   Equals to `°`, `′` and `″`.
## \_\_author\_\_
   The author of this package.
# Submodule
  - ### _degrees_.trigonometry
     A submodule for trigonometric functions.
     Supported functions:

     | `sin` | `cos` | `tan` | `asin` | `acos` | `atan` |
     |-------|-------|-------|--------|--------|--------|
     | `cot` | `sec` | `csc` | `acot` | `asec` | `acsc` |
     
     The functions start with `a` are inverse trigonometric functions, and the others are forward trigonometric
functions. Here is the input types and return types of these functions:<br>
     `def forward_trigonometric_function(x: Degree) -> float: ...`<br>
     `def inverse_trigonometric_function(x: int | float) -> Degree: ...`

# Changelog
   1. Added trigonometric functions.
# Older versions
> Looking for src and a README older version?<br>
> Click [here](https://github.com/ArcticChar-Zhang/degrees/commits/main/) for V0.4.1+(include V0.4.1), next click the
> version you want, and then click "📄Browse files".<br>
> And [here](https://pypi.org/project/degrees/#history) for versions below V0.4.1.

> ### Write in the end
> If you found the bug in the code, you can email me at `snake830@vip.163.com`. I am happy to receive the advice!
