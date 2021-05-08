# 0x01. Python - if/else, loops, functions

## Overview
This project introduced us to how to use various conditionals and loops in Python including `if`, `if...else`, `while`, `for`, `break`, `continue`, `pass`, `range`, and `return`. It also introduced us to variable scope and basic arithmetic operators.

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

### C Scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be compiled on Ubuntu 14.04 LTS
* Your programs and functions will be compiled with gcc 4.8.4 using the flags `-Wall -Werror -Wextra and -pedantic`
* All your files should end with a new line
* Your code should use the Betty style. It will be checked using `betty-style.pl` and `betty-doc.pl`
* You are not allowed to use global variables
* No more than 5 functions per file
* The prototypes of all your functions should be included in your header file called `lists.h`
* All your header files should be include guarded

## Tasks
### Mandatory
**[0-positive_or_negative.py](0-positive_or_negative.py)** - This program will assign a random number to variable `number` using the following [source code](https://intranet.hbtn.io/rltoken/2S3G4vOnRrWymCjKYd6Wew). The output to be printed would be the number followed by:
* `is positive` if the number is greater than 0
* `is zero` if the number is 0
* `is negative` if the number is less than 0
```
vagrant:0x01-python-if_else_loops_functions$ ./0-positive_or_negative.py
4 is positive
vagrant:0x01-python-if_else_loops_functions$ ./0-positive_or_negative.py
-1 is negative
vagrant:0x01-python-if_else_loops_functions$ ./0-positive_or_negative.py
7 is positive
vagrant:0x01-python-if_else_loops_functions$ ./0-positive_or_negative.py
-3 is negative
vagrant:0x01-python-if_else_loops_functions$ ./0-positive_or_negative.py
-1 is negative
```
**[1-last_digit.py](1-last_digit.py)** - This program will assign a random number to variable `number` using the following [source code](https://intranet.hbtn.io/rltoken/e9k9---MJXcMmIjlMdlBpw). The output of the program will be:
* `Last digit of` followed by:
  * The number
    * The string `is`
      * `and is greater than 5` if the number is greater than 5
        * `and is 0` if the number is 0
	  * `and is less than 6 and not 0` if the string is less than 6 and not 0
	  ```
	  vagrant:0x01-python-if_else_loops_functions$ ./1-last_digit.py
	  Last digit of 9424 is 4 and is less than 6 and not 0
	  vagrant:0x01-python-if_else_loops_functions$ ./1-last_digit.py
	  Last digit of 318 is 8 and is greater than 5
	  vagrant:0x01-python-if_else_loops_functions$ ./1-last_digit.py
	  Last digit of -7147 is -7 and is less than 6 and not 0
	  ```
	  **[2-print_alphabet.py](2-print_alphabet.py)** - Prints the lowercase alphabet not followed by a newline using:
	  * one loop
	  * `print` once
	  * no characters stored in variables
	  * no imported modules
	  ```
	  vagrant:0x01-python-if_else_loops_functions$ ./2-print_alphabet.py
	  abcdefghijklmnopqrstuvwxyzvagrant:0x01-python-if_else_loops_functions$
	  ```
	  **[3-print_alphabt.py](3-print_alphabt.py)** - Prints the alphabet in lowercase not followed by a new line
	  * Print all letters except `q` and `e`
	  * `print` once
	  * one loop
	  * no characters stored in variables
	  * no imported modules
	  ```
	  vagrant:0x01-python-if_else_loops_functions$ ./3-print_alphabt.py
	  abcdfghijklmnoprstuvwxyzvagrant:0x01-python-if_else_loops_functions$
	  ```
	  **[4-print_hexa.py](4-print_hexa.py)** - Prints all numbers from 0 to 98 in decimal and in hexadecimal
	  * `print` once
	  * one loop
	  * no characters or numbers stored in variables
	  * no imported modules
	  ```
	  vagrant:0x01-python-if_else_loops_functions$ ./4-print_hexa.py
	  0 = 0x0
	  1 = 0x1
	  2 = 0x2
	  3 = 0x3
	  4 = 0x4
	  5 = 0x5
	  6 = 0x6
	  7 = 0x7
	  8 = 0x8
	  9 = 0x9
	  10 = 0xa
	  ...
	  90 = 0x5a
	  91 = 0x5b
	  92 = 0x5c
	  93 = 0x5d
	  94 = 0x5e
	  95 = 0x5f
	  96 = 0x60
	  97 = 0x61
	  98 = 0x62
	  ```
	  **[5-print_comb2.py](5-print_comb2.py)** - Prints the numbers from 0 to 99
	  * numbers separated by commas and a space
	  * numbers printed in ascending order with two digits
	  * last number followed by new line
	  *`print` twice
	  * one loop
	  * no stored numbers or strings in variables
	  * no imported modules
	  ```
	  vagrant:0x01-python-if_else_loops_functions$ ./5-print_comb2.py
	  00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
	  ```
	  **[6-print_comb3.py](6-print_comb3.py)** - Prints all possible different combinations of two digits
	  * numbers separated by commas and a space
	  * two digits must be different
	  * the smallest combination of two digits is the one printed
	  * numbers printed in ascending order with two digits
	  * last number followed by a new line
	  * `print` three times
	  * 2 loops
	  * no stored values in variables
	  * no imported modules
	  ```
	  vagrant:0x01-python-if_else_loops_functions$ ./6-print_comb3.py
	  01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
	  ```
	  **[7-islower.py](7-islower.py)** - Checks if a character is lowercase
	  * returns `True` if it is lowercase
	  * returns `False` otherwise
	  * no imported modules
	  * cannot use `str.upper()` and `str.isupper()`
	  ```
	  vagrant:0x01-python-if_else_loops_functions$ ./7-main.py
	  a is lower
	  H is upper
	  A is upper
	  3 is upper
	  g is lower
	  ```
	  **[8-uppercase.py](8-uppercase.py)** - Prints a string in uppercase
	  * `print` twice
	  * one loop
	  * no imported modules
	  * cannot use `str.upper()` or `str.isupper()`
	  ```
	  vagrant:0x01-python-if_else_loops_functions$ ./8-main.py
	  DHK
	  DHK SCHOOL 98 BATTERY STREET
	  ```
	  **[9-print_last_digit.py](9-print_last_digit.py)** - Prints the last digit of a number and returns the last digit
	  * no imported modules
	  ```
	  vagrant:0x01-python-if_else_loops_functions$ ./9-main.py
	  8044
	  ```
	  **[10-add.py](10-add.py)** - Adds two integers and returns the result
	  * no imported modules
	  ```
	  vagrant:0x01-python-if_else_loops_functions$ ./10-main.py
	  7
	  98
	  98
	  ```
	  **[11-pow.py](11-pow.py)** - Computes the power of two integers and returns the result
	  * no imported modules
	  ```
	  vagrant:0x01-python-if_else_loops_functions$ ./11-main.py
	  4
	  9604
	  1
	  0.0001
	  -1024
	  ```
	  **[12-fizzbuzz.py](12-fizzbuzz.py)** - Prints the numbers 1 to 100 separated by spaces using `FizzBuzz` rules
	  * numbers which are multiples of 3 - print `Fizz`
	  * numbers which are multiples of 5 - print `Buzz`
	  * numbers which are multiples of 3 and 5 - print `FizzBuzz`
	  ```
	  vagrant:0x01-python-if_else_loops_functions$ ./12-main.py
	  1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz
	  ```
	  **[13-insert_number.c](13-insert_number.c)** - Inserts a number into a sorted linked list
	  ```
	  vagrant:0x01-python-if_else_loops_functions$ ./insert
	  0
	  1
	  2
	  3
	  4
	  98
	  402
	  1024
	  -----------------
	  -500
	  0
	  0
	  1
	  1
	  2
	  3
	  4
	  27
	  98
	  402
	  1024
	  1025
	  ```
	  **[lists.h](lists.h)** - the header file for 13-insert_number.c

	  ### Advanced
	  **[100-print_tebahpla.py](100-print_tebahpla.py)** - prints the alphabet in reverse order, alternating lowercase and uppercase
	  * `print` once
	  * one loop
	  * no stored characters in variables
	  * no imported modules
	  ```
	  vagrant:0x01-python-if_else_loops_functions$ ./100-print_tebahpla.py
	  zYxWvUtSrQpOnMlKjIhGfEdCbAvagrant:0x01-python-if_else_loops_functions$
	  ```
	  **[101-remove_char_at.py](101-remove_char_at.py)** - Creates a copy of the string and removes a character at a specified position
	  ```
	  vagrant:0x01-python-if_else_loops_functions$ ./101-main.py
	  Holerton School
	  Chcago
	   is fun!
	   School
	   Python
	   ```
	   **[102-magic_calculation.py](102-magic_calculation.py)** - Translation of the following Python bytecode into a Python script
	   ```
	     3           0 LOAD_FAST                0 (a)
	                   3 LOAD_FAST                1 (b)
			                 6 COMPARE_OP               0 (<)
					               9 POP_JUMP_IF_FALSE       16

						         4          12 LOAD_FAST                2 (c)
							              15 RETURN_VALUE

								        5     >>   16 LOAD_FAST                2 (c)
									             19 LOAD_FAST                1 (b)
										                  22 COMPARE_OP               4 (>)
												               25 POP_JUMP_IF_FALSE       36

													         6          28 LOAD_FAST                0 (a)
														              31 LOAD_FAST                1 (b)
															                   34 BINARY_ADD
																	                35 RETURN_VALUE

																			  7     >>   36 LOAD_FAST                0 (a)
																			               39 LOAD_FAST                1 (b)
																				                    42 BINARY_MULTIPLY
																						                 43 LOAD_FAST                2 (c)
																								              46 BINARY_SUBTRACT
																									                   47 RETURN_VALUE
																											   ```

																											   2021 - All programs written by itsmuriuki