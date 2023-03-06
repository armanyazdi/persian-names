# persian-names

[![PyPI](https://img.shields.io/pypi/v/persian-names?style=for-the-badge)](https://pypi.org/project/persian-names)
[![GitHub](https://img.shields.io/github/license/armanyazdi/persian-names?style=for-the-badge)](https://pypi.org/project/persian-names)

A Python library for generating random Persian (Farsi) names.

This package generates frequently logical names 
(a mix of popular Persian and Arabic names with common Persian family name suffixes).

## Installation

Install from [PyPI](https://pypi.org/project/persian-names) with pip by typing in your favorite terminal:

`pip install persian-names`

## Usage

Let's take a look at what an example test case would look like using `persian-names`.

### Generate Persian Full Names in Farsi:

```python
from persian_names import fullname_fa

fullname_fa('male')   # or fullname_fa('m')
fullname_fa('female') # or fullname_fa('f')
fullname_fa('random') # or fullname_fa('r')
```

#### Example:

```python
from persian_names import fullname_fa

print(fullname_fa('m')) # اشکان محمدرضائیان
print(fullname_fa('f')) # مهسا امینی
print(fullname_fa('r')) # بیتا خسروی راد
```

### Generate Persian Full Names in English:

```python
from persian_names import fullname_en

fullname_en('male')   # or fullname_en('m')
fullname_en('female') # or fullname_en('f')
fullname_en('random') # or fullname_en('r')
```

#### Example:

```python
from persian_names import fullname_en

print(fullname_en('m')) # Arsalan Mohammadi
print(fullname_en('f')) # Sara Alipour
print(fullname_en('r')) # Danial Ferdosi
```

### Generate First Names and Last Names in Farsi:

```python
from persian_names import *

# First Name
firstname_fa('male')   # or firstname_fa('m')
firstname_fa('female') # or firstname_fa('f')
firstname_fa('random') # or firstname_fa('r')

# Last Name
lastname_fa()
```

#### Example:

```python
from persian_names import *

print(firstname_fa('m')) # آرمان
print(firstname_fa('f')) # ساحل
print(firstname_fa('r')) # علیرضا
print(lastname_fa())     # شیخ اسماعیلی
```

### Generate First Names and Last Names in English:

```python
from persian_names import *

# First Name
firstname_en('male')   # or firstname_en('m')
firstname_en('female') # or firstname_en('f')
firstname_en('random') # or firstname_en('r')

# Last Name
lastname_en()
```

#### Example:

```python
from persian_names import *

print(firstname_en('m')) # Mehrad
print(firstname_en('f')) # Darya
print(firstname_en('r')) # Baran
print(lastname_en())     # Bakhtiarizadeh
```

## License

`persian-names` is available under the [MIT license](https://github.com/armanyazdi/persian-names/blob/main/LICENSE).