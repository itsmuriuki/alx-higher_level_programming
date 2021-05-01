# 0x02. Python - import & modules

## Overview
This project concerns the subject of importing functions from other files, creating modules, using the `dir()` function, preventing scripts from being executed when importing, and command line arguments `argv` with Python programs.

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

## Tasks
### Mandatory
**[0-add.py](0-add.py)** - Imports a function `def add(a, b):` from a file `add_0.py` and prints the result of the addition `1 + 2 = 3`.
* We must define `a` and `b` in two different lines
* The print format is `<a value> + <b value> = <add(a, b) value>`
* We must make sure the code is not executed when using `__import__`
```
vagrant:0x02-python-import_modules$ ./0-add.py
1 + 2 = 3
```
**[1-calculation.py](1-calculation.py)** - Imports functions from a file called `calculator_1.py` and does some mathematical operations.
* Values `10` and `5` must be stored in `a` and `b` respectively
* We must make sure the code is not executed when using `__import__`
```
vagrant:0x02-python-import_modules$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
```
**[2-args.py](2-args.py)** - Prints the number of and the list of arguments called with this program. Out put is, for example, `1 argument:` on one line followed by a list of arguments `1: Hello`.
* The code must not be executed at import
* One line per argument
```
vagrant:0x02-python-import_modules$ ./2-args.py
0 arguments.
vagrant:0x02-python-import_modules$ ./2-args.py Hello
1 argument:
1: Hello
vagrant:0x02-python-import_modules$ ./2-args.py Hello World! Derek Kwok
4 arguments:
1: Hello
2: World!
3: Derek
4: Kwok
```
**[3-infinite_add.py](3-infinite_add.py)** - Prints the resut of addition of all arguments given to it
* Code should not be executed at import
```
vagrant:0x02-python-import_modules$ ./3-infinite_add.py 5 10 15 20
50
vagrant:0x02-python-import_modules$ ./3-infinite_add.py  100000000000000000000000000
000000000000000 20000000000000000000000000000000000000000000000000000000000000000000
20000000000000000000000000100000000000000000000000000000000000000000
```
**[4-hidden_discovery.py](4-hidden_discovery.py)** - Prints all names defined by the compiled module `hidden_4.pyc`
* One name per line, in alphabetical order
* Only names that do not start with `__` are printed
* Code should not be executed at import
```
vagrant:0x02-python-import_modules$ ./4-hidden_discovery.py
my_secret_santa
print_dhk
print_school
```
**[5-variable_load.py](5-variable_load.py)** - Imports the variable `a` from a file called `variable_load_5.py` and prints its value
* Code should not be executed at import
```
vagrant:0x02-python-import_modules$ ./5-variable_load.py
98
```
### Advanced
**[100-my_calculator.py](100-my_calculator.py)** - Imports all functions from a file called `calculator_1.py` and handles basic operations.
* Operators can be addition, subtraction, multiplication, and division
* Throws error messages if number of arguments is not 3
* Throws error messages if the sign is not one of the four above
* Code should not be executed when imported
```
vagrant:0x02-python-import_modules$ ./100-my_calculator.py 5 + 5
5 + 5 = 10
vagrant:0x02-python-import_modules$ ./100-my_calculator.py  5 - 5
5 - 5 = 0
vagrant:0x02-python-import_modules$ ./100-my_calculator.py  5 \* 5
5 * 5 = 25
vagrant:0x02-python-import_modules$ ./100-my_calculator.py  5 / 5
5 / 5 = 1
```
**[101-easy_print.py](101-easy_print.py)** - Program prints `#pythoniscool` followed by a new line in standard output
* Program must be maximum 2 lines long
```
vagrant:0x02-python-import_modules$ ./101-easy_print.py
#pythoniscool
```
**[102-magic_calculation.py](102-magic_calculation.py)** - Translation of Python bytecode into a Python script.
```
  3           0 LOAD_CONST               1 (0)
                3 LOAD_CONST               2 (('add', 'sub'))
		              6 IMPORT_NAME              0 (magic_calculation_102)
			                    9 IMPORT_FROM              1 (add)
					                 12 STORE_FAST               2 (add)
							              15 IMPORT_FROM              2 (sub)
								                   18 STORE_FAST               3 (sub)
										                21 POP_TOP

												  4          22 LOAD_FAST                0 (a)
												               25 LOAD_FAST                1 (b)
													                    28 COMPARE_OP               0 (<)
															                 31 POP_JUMP_IF_FALSE       94

																	   5          34 LOAD_FAST                2 (add)
																	                37 LOAD_FAST                0 (a)
																			             40 LOAD_FAST                1 (b)
																				                  43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
																						               46 STORE_FAST               4 (c)

																							         6          49 SETUP_LOOP              38 (to 90)
																								              52 LOAD_GLOBAL              3 (range)
																									                   55 LOAD_CONST               3 (4)
																											                58 LOAD_CONST               4 (6)
																													             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
																														                  64 GET_ITER
																																          >>   65 FOR_ITER                21 (to 89)
																																	               68 STORE_FAST               5 (i)

																																		         7          71 LOAD_FAST                2 (add)
																																			              74 LOAD_FAST                4 (c)
																																				                   77 LOAD_FAST                5 (i)
																																						                80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
																																								             83 STORE_FAST               4 (c)
																																									                  86 JUMP_ABSOLUTE           65
																																											          >>   89 POP_BLOCK

																																												    8     >>   90 LOAD_FAST                4 (c)
																																												                 93 RETURN_VALUE

																																														  10     >>   94 LOAD_FAST                3 (sub)
																																														               97 LOAD_FAST                0 (a)
																																															                   100 LOAD_FAST                1 (b)
																																																	               103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
																																																		                   106 RETURN_VALUE
																																																				               107 LOAD_CONST               0 (None)
																																																					                   110 RETURN_VALUE
																																																							   ```

																																																							   **[103-fast_alphabet.py](103-fast_alphabet.py)** - Prints the alphabet in uppercase followed by a new line
																																																							   * Must be a maximum of 3 lines long
																																																							   ```
																																																							   vagrant:0x02-python-import_modules$ ./103-fast_alphabet.py
																																																							   ABCDEFGHIJKLMNOPQRSTUVWXYZ
																																																							   ```

																																																							   2021 - All programs written by itsmuriuki