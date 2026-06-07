# degrees V0.4.1b1
# Contents
* Introduction
* Importing
* Class
  * Degree
* Functions
  * degree2radian
  * radian2degree
  * normalize
* Changelog
# Introduction
### A Python library for degree calculations and conversions.
> [!TIP]
> ### **Added in version 0.2:** Supported `pickle`.
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
   > The `complex(degree_obj)` is different from `degree_obj.to_complex(length)`. The former returns
   `int(degree_obj)+0j`, but the latter returns `complex(length * cos(theta), length * sin(theta))`,
   `theta=degree2radian(degree_obj)`.

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

  - ### _staticmethod_ from_str(string)
     Return a degree object from a string. The **dms** characters should be **`°`, `'` and `"`**.
  - ### _staticmethod_ from_unicode(string)
     Similar to `from_str`, but the **dms** characters should be **`°`, `′` and `″`**.
   > [!TIP]
   > **Added in version 0.1.10.**
  - ### _staticmethod_ from_iter(iterable)
     Return a degree object from an iterable.
  - ### total_seconds
     The total seconds of a degree object.
  - ### _property_ deg
     The degree of a degree object(without sign).
  - ### _property_ min
     The minute of a degree object(without sign).
  - ### _property_ sec
     The second of a degree object(without sign).
  - ### _property_ sign
     The sign of a degree object.
  - ### to_complex(length: int | float)
     Returns the complex number corresponding to `(angle=self, radius=length)`.
   > [!TIP]
   > **Added in version 0.2.1.**
  - ### _property_ dms
     A tuple of `(degree, minute, second)`.
   
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
# Changelog
   1. Changed `deg`, `min`, `sec` and `sign` to `property`.
   2. Added `__author__`.
   3. Uploaded to `GitHub`.
> ### Write in the end
> If you found the bug in the code, you can email me at `snake830@vip.163.com`. I am happy to receive the advice!
