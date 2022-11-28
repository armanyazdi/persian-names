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
import persian_names as pn

pn.fullname_fa('male')   # or pn.fullname_fa('m')
pn.fullname_fa('female') # or pn.fullname_fa('f')
pn.fullname_fa('random') # or pn.fullname_fa('r')
```

#### Example:

```python
import persian_names as pn

male = pn.fullname_fa('m')
female = pn.fullname_fa('f')
random = pn.fullname_fa('r')

print('Male name:', male)     # Male name: اشکان محمدرضائیان
print('Female name:', female) # Female name: مهسا امینی
print('Random name:', random) # Random name: بیتا خسروی راد
```

### Generate Persian names in English:

```python
import persian_names as pn

pn.fullname_en('male')   # or pn.fullname_en('m')
pn.fullname_en('female') # or pn.fullname_en('f')
pn.fullname_en('random') # or pn.fullname_en('r')
```

#### Example:

```python
import persian_names as pn

male = pn.fullname_en('m')
female = pn.fullname_en('f')
random = pn.fullname_en('r')

print('Male name:', male)     # Male name: Arsalan Mohammadi
print('Female name:', female) # Female name: Sara Alipour
print('Random name:', random) # Random name: Danial Ferdosi
```