# 0x05. Python - Exceptions

## Overview
This project is about Python exceptions and error handling. It stresses the use of `try/except`, raises exceptions, catching exceptions, and implementing cleanup actions. Additionally, a large portion of the project deals with how to handle exceptions.

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
**[0-safe_print_list.py](0-safe_print_list.py)** - Prints `x` elements of a list
* All elements printed on the same line
* Use `try:/ except:`
* no imported module
* `x` can be bigger than the length of the list
```
vagrant:0x05-python-exceptions$ ./0-main.py
12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5
```

**[1-safe_print_integer.py](1-safe_print_integer.py)** - Prints an integer with `{:d}.format()`
* Returns `True` if value was correctly printed, otherwise it returns false
* Must use `try/except`
* no imported module
```
vagrant:0x05-python-exceptions$ ./1-main.py
[1, 2, 3] is not an integer
-89
DHK is not an integer
```

**[2-safe_print_list_integers.py](2-safe_print_list_integers.py)** - Prints the first `x` elements of a list and only if they are integers
* no imported module
* same requirements as `0-safe_print_list.py`
```
vagrant:0x05-python-exceptions$ ./2-main.py
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File "./2-main.py", line 14, in <module>
      nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
        File "/home/vagrant/dhkschool-higher_level_programming/0x05-python-exceptions/2-safe_print_list_integers.py", line 6, in safe_print_list_integers
	    print("{:d}".format(my_list[i]), end='')
	    IndexError: list index out of range
	    ```

	    **[3-safe_print_division.py](3-safe_print_division.py)** - Divides 2 integers and prints the result
	    * Returns value of division, otherwise `None`
	    * Use `{}.format()` to print the result
	    * no imported module
	    ```
	    vagrant:0x05-python-exceptions$ ./3-main.py
	    Inside result: 6.0
	    12 / 2 = 6.0
	    Inside result: None
	    12 / 0 = None
	    ```

	    **[4-list_division.py](4-list_division.py)** - Divides a list by another list
	    * If elements cannot be divided, resut of division is 0
	    * Error handling if wrong data type, if division cannot be done, or if lists are too short
	    * no imported module
	    ```
	    vagrant:0x05-python-exceptions$ ./4-main.py
	    [5.0, 2.0, 1.0]
	    --
	    division by 0
	    wrong type
	    out of range
	    [5.0, 0, 0, 2.0, 0]
	    ```

	    **[5-raise_exception.py](5-raise_exception.py)** - Raises a type exception
	    ```
	    vagrant:0x05-python-exceptions$ ./5-main.py
	    Exception raised
	    ```

	    **[6-raise_exception_msg.py](6-raise_exception_msg.py)** - Raises a name exception with a message
	    ```
	    vagrant:0x05-python-exceptions$ ./6-main.py
	    C is fun
	    ```

	    ### Advanced
	    **[100-safe_print_integer_err.py](100-safe_print_integer_err.py)** - Prints an integer with an error message
	    * Returns `True` if the value was correctly printed
	    * If `False` is returned, it prints a message to `stderr`
	    ```
	    vagrant:0x05-python-exceptions$ ./100-main.py
	    89
	    -89
	    Exception: Unknown format code 'd' for object of type 'str'
	    DHK is not an integer
	    ```

	    **[101-safe_function.py](101-safe_function.py)** - Executes a function safely
	    * Returns `None` if something happens and prints a message, otherwise, return the result of the function
	    * Use `try/except`
	    ```
	    vagrant:0x05-python-exceptions$ ./101-main.py
	    result of my_div: 5.0
	    Exception: division by zero
	    result of my_div: None
	    1
	    2
	    3
	    4
	    Exception: list index out of range
	    result of print_list: None
	    ```

	    **[102-magic_calculation.py](102-magic_calculation.py)** - Translation of Python bytecode into a Python script
	    ```
	      3           0 LOAD_CONST               1 (0)
	            	  3 STORE_FAST               2 (result)

	      4           6 SETUP_LOOP              94 (to 103)
			  9 LOAD_GLOBAL              0 (range)
			  12 LOAD_CONST               2 (1)
			  15 LOAD_CONST               3 (3)
			  18 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
			  21 GET_ITER
			  >>   22 FOR_ITER                77 (to 102)
			  25 STORE_FAST               3 (i)

	       5          28 SETUP_EXCEPT            49 (to 80)

	       6          31 LOAD_FAST                3 (i)
			  34 LOAD_FAST                0 (a)
			  37 COMPARE_OP               4 (>)
			  40 POP_JUMP_IF_FALSE       58

	       7          43 LOAD_GLOBAL              1 (Exception)
			  46 LOAD_CONST               4 ('Too far')
			  49 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
			  52 RAISE_VARARGS            1
			  55 JUMP_FORWARD            18 (to 76)

	       9     >>   58 LOAD_FAST                2 (result)
			  61 LOAD_FAST                0 (a)
			  64 LOAD_FAST                1 (b)
			  67 BINARY_POWER
			  68 LOAD_FAST                3 (i)
			  71 BINARY_TRUE_DIVIDE
			  72 INPLACE_ADD
			  73 STORE_FAST               2 (result)
			  >>   76 POP_BLOCK
			  77 JUMP_ABSOLUTE           22

	      10     >>   80 POP_TOP
			  81 POP_TOP
			  82 POP_TOP

	      11          83 LOAD_FAST                1 (b)
			  86 LOAD_FAST                0 (a)
			  89 BINARY_ADD
			  90 STORE_FAST               2 (result)

	      12          93 BREAK_LOOP
			  94 POP_EXCEPT
			  95 JUMP_ABSOLUTE           22
			  98 END_FINALLY
			  99 JUMP_ABSOLUTE           22
			  >>  102 POP_BLOCK

			  13     >>  103 LOAD_FAST                2 (result)
			  106 RETURN_VALUE
			  ```
2021 - All programs written by itsmuriuki