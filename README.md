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

### Generate Persian names in Farsi:

```python
from persian_names import *

fullname_fa('male')   # or fullname_fa('m')
fullname_fa('female') # or fullname_fa('f')
fullname_fa('random') # or fullname_fa('r')
```

#### Example:

```python
from persian_names import *

print('Male:', fullname_fa('m'))   # Male: اشکان محمدرضائیان
print('Female:', fullname_fa('f')) # Female: مهسا امینی
print('Random:', fullname_fa('r')) # Random: بیتا خسروی راد
```

### Generate Persian names in English:

```python
from persian_names import *

fullname_en('male')   # or fullname_en('m')
fullname_en('female') # or fullname_en('f')
fullname_en('random') # or fullname_en('r')
```

#### Example:

```python
from persian_names import *

print('Male:', fullname_en('m'))   # Male: Arsalan Mohammadi
print('Female:', fullname_en('f')) # Female: Sara Alipour
print('Random:', fullname_en('r')) # Random: Danial Ferdosi
```