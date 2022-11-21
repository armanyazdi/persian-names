# persian-names

A Python library for generating random Persian (Farsi) names.

# Installation

Install from PyPI with pip by typing in your favorite terminal:

`pip install persian-names`

# Usage

Let's take a look at what an example test case would look like using `persian-names`.

#### Generate Persian names in Farsi:

```python
import persian_names as pn

pn.fullname_fa('male')   # or pn.fullname_fa('m')
pn.fullname_fa('female') # or pn.fullname_fa('f')
pn.fullname_fa('random') # or pn.fullname_fa('r')
```
Example:
```python
import persian_names as pn

male = pn.fullname_fa('m')
female = pn.fullname_fa('f')
random = pn.fullname_fa('r')

print('Male name:', male)
print('Female name:', female)
print('Random name:', random)
```
Response:
```
Male name: اشکان محمدرضائیان
Female name: مهسا امینی
Random name: بیتا خسروی راد
```

#### Generate Persian names in English:

```python
import persian_names as pn

pn.fullname_en('male')   # or pn.fullname_en('m')
pn.fullname_en('female') # or pn.fullname_en('f')
pn.fullname_en('random') # or pn.fullname_en('r')
```
Example:
```python
import persian_names as pn

male = pn.fullname_en('m')
female = pn.fullname_en('f')
random = pn.fullname_en('r')

print('Male name:', male)
print('Female name:', female)
print('Random name:', random)
```
Response:
```
Male name: Arsalan Mohammadi
Female name: Sara Alipour
Random name: Danial Ferdosi
```