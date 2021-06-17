# 0x07. Python - Test-driven development

## Overview
This project focused on Test-Driven Development (TDD) and the associated test modules in Python such as `doctest` and `unittest`. We were tasked with coming up with a variety of tests for the few scripts in this project in an attempt to pass the project without a code checker, as we would normally be provided with.

## Requirements
### Python Scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the PEP 8 style (version 1.7.*)
* All your files must be executable
* The length of your files will be tested using `wc`

### Python Test Cases
* Allowed editors: `vi`, `vim`, `emacs`
* All your files should end with a new line
* All your test files should be inside a folder `tests`
* All your test files should be text files (extension: `.txt`)
* All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)

## Tasks
### Mandatory
**[0-add_integer.py](0-add_integer.py)** - Adds two integers
* [Test File](tests/0-add_integer.txt)
* Throws errors if the numbers are not integers or floats
* Floats must be typecasted into ints
```
vagrant:0x07-python-test_driven_development$ ./0-main.py
3
98
100
98
b must be an integer
a must be an integer
```

**[2-matrix_divided.py](2-matrix_divided.py)** - Divides all elements of a matrix
* [Test File](tests/2-matrix_divided.txt)
* Throws errors if matrix is not a list of list of integers or floats
* Throws error if there are rows with differing sizes
* Throws an error if `div` is not an integer or float, or if it is 0
* All elements rounded to 2 decimal places
```
vagrant:0x07-python-test_driven_development$ ./2-main.py
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
[[1, 2, 3], [4, 5, 6]]
```

**[3-say_my_name.py](3-say_my_name.py)** - Prints the string `My name is <first name> <last name>`
* [Test File](tests/3-say_my_name.txt)
* If the two arguments are not strings, throws an error
* no imported module
```
vagrant:0x07-python-test_driven_development$ ./3-main.py
My name is John Smith
My name is Walter White
My name is Bob
```

**[4-print_square.py](4-print_square.py)** - Prints a square with a character `#`
* [Test File](tests/4-print_square.txt)
* If the size is not an integer or if it is less than 0, throws an error
* no imported module
```
vagrant:0x07-python-test_driven_development$ ./4-main.py
####
####
####
####

##########
##########
##########
##########
##########
##########
##########
##########
##########
##########


#
```

**[5-text_indentation.py](5-text_indentation.py)** - Prints a text with 2 new lines after `.`, `?`, or `:`.
* [Test File](tests/5-text_indentation.txt)
* If the text is not a string, throws an error
* There should be no leading or trailing whitespace on any printed strings
* no imported module
```
vagrant:0x07-python-test_driven_development$ ./5-main.py
Lorem ipsum dolor sit amet, consectetur adipiscing elit.

Quonam modo?

Utrum igitur tibi litteram videor an totas paginas commovere?

Non autem hoc:

igitur ne illud quidem.

Fortasse id optimum, sed ubi illud:

Plus semper voluptatis?

Teneo, inquit, finem illi videri nihil dolere.

Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.

Si id dicis, vicimus.

Inde sermone vario sex illa a Dipylo stadia confecimus.

Sin aliud quid voles, postea.

Quae animi affectio suum cuique tribuens atque hanc, quam dico.

Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres
```

**[tests/6-max_integer_test.py](tests/6-max_integer_test.py)** - A unittest module for a maximum integer program
* Should be executed with the command `python3 -m unittest tests.6-max_integer_test`
```
vagrant:0x07-python-test_driven_development$ python3 -m unittest tests.6-max_integer
_test
.....
----------------------------------------------------------------------
Ran 5 tests in 0.003s

OK

```

2021- All programs written by itsmuriuki
