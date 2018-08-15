# Dictlisttools
###### version 1.0
###### Anthony Blanchflower

Functions which operate on lists of dictionaries.


## Getting Started

These instructions will allow you to import dictlisttools as a Python module.
For creating a distribution see the Deployment section of this document.

### Prerequisites

If you do not have git installed, install it from https://git-scm.com/downloads.
If you do not have pip installed, install it from https://pip.pypa.io.

Make sure you have the latest versions of setuptools and wheel installed:

```
python3 -m pip install --user --upgrade setuptools wheel
```

If you have trouble installing setuptools and wheel visit
https://packaging.python.org/tutorials/installing-packages/

### Installing

Dictlisttools can be installed as a python module using the pip installer.

```
$ pip install git+git://github.com/anthonyblanchflower/dictlisttools.git
```

## Documentation

These instruction will allow you to call functions from the dictlisttools module.

### Using Dictlisttools

First import module:

```
import dictlisttools
```

Now you can use the dictlisttools functions.

### Module functions

dictlisttools.sortbykey( dictionary, key)

Sort a list of dictionaries by a common key and return the sorted list.

```
sortbykey([{'A': 3}, {'A': 1}, {'A': 2}], 'A')
```

###### Parameters:

dictionary: a list of dictionaries sharing a common key

key: a dictionary key used to sort the list of dictionaries

###### Returns:

```
[{'A': 1}, {'A': 2}, {'A': 3}]
```

## Running the tests

Tests can be run using the following command:

```
python3 setup.py test
```

## Deployment

A distribution package can be generated using the following command:

```
python3 setup.py sdist bdist_wheel
```
