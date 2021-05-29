# 0x03. Python - Data Structures: Lists, Tuples

## Overview
This project concerns the subject of data structures such as lists, strings, tuples, tuple packing/unpacking, list comprehensions, tuples vs lists, strings vs lists, and common methods associated with lists.

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
**[0-print_list_integer.py](0-print_list_integer.py)** - Prints all integers of a list
* One integer per line
* No imported modules
* Assumption: List contains only integers
* Must use `str.format()`
```
vagrant:0x03-python-data_structures$ ./0-main.py
1
2
3
4
5
```

**[1-element_at.py](1-element_at.py)** - Retrieves an element from a list
* If `idx` is negative, return `None`
* if `idx` is out of range, return `None`
* no imported modules
```
vagrant:0x03-python-data_structures$ ./1-main.py
Element at index 3 is 4
```

**[2-replace_in_list.py](2-replace_in_list.py)** - Replaces an element of a list at a specific position
* If `idx` is negative, return original list
* If `idx` is out of range, return original list
* no imported modules
```
vagrant:0x03-python-data_structures$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
```

**[3-print_reversed_list_integer.py](3-print_reversed_list_integer.py)** - Prints all integers of a list in reverse order
* one int per line
* no imported modules
* Assumption: List contains only integers
* must use `str.format()`
```
vagrant:0x03-python-data_structures$ ./3-main.py
5
4
3
2
1
```

**[4-new_in_list.py](4-new_in_list.py)** - Replaces an element in a list at a specific position without modifying the original list
* If `idx` is negative, return original list
* If `idx` is out of range, return original list
* no imported modules
```
vagrant:0x03-python-data_structures$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
```

**[5-no_c.py](5-no_c.py)** - Removes all `C` and `c` from a string
* Return the new string
* no imported modules
```
vagrant:0x03-python-data_structures$ ./5-main.py
DHK Shool
hiago
 is fun!
 ```

 **[6-print_matrix_integer.py](6-print_matrix_integer.py)** - Prints a matrix of integers
 * no imported modules
 * Assumption: list only contains integers
 * Must use `str.format()`
 ```
 vagrant:0x03-python-data_structures$ ./6-main.py
 1 2 3
 4 5 6
 7 8 9
 --

 ```

 **[7-add_tuple.py](7-add_tuple.py)** - Adds 2 tuples where the first element of the returned tuple is the addition of the first element of each argument and the second element is the addition of the second element of each argument
 * no imported modules
 * Assumption: tuples only contain integers
 * If tuple is smaller than 2, use value 0 for the missing integers
 * If tuple is bigger than 2, use only the first integers
 ```
 vagrant:0x03-python-data_structures$ ./7-main.py
 (89, 100)
 (2, 89)
 (1, 89)
 ```

 **[8-multiple_returns.py](8-multiple_returns.py)** - Returns tuple with the length of a string and its first character
 * If sentence is empty, first character should be equal to `None`
 * no imported modules
 ```
 vagrant:0x03-python-data_structures$ ./8-main.py
 Length: 32 - First character: A
 ```

 **[9-max_integer.py](9-max_integer.py)** - Finds the biggest integer of a list
 * Empty list - return `None`
 * Assumption: list contains only integers
 * no imported modules
 * no use of `max()` builtin
 ```
 vagrant:0x03-python-data_structures$ ./9-main.py
 Max: 90
 ```

 **[10-divisible_by_2.py](10-divisible_by_2.py)** - Finds all multiples of 2 in a list and returns `True` or `False` depending on whether they are divisible by 2
 * new list should be the same size as original list
 * no imported module
 ```
 vagrant:0x03-python-data_structures$ ./10-main.py
 0 is divisible by 2
 1 is not divisible by 2
 2 is divisible by 2
 3 is not divisible by 2
 4 is divisible by 2
 5 is not divisible by 2
 6 is divisible by 2
 ```

 **[11-delete_at.py](11-delete_at.py)** - Deletes the item at a specific position in a list
 * if `idx` is negative or out of range, nothing changes
 * no imported module
 ```
 vagrant:0x03-python-data_structures$ ./11-main.py
 [1, 2, 3, 4, 5]
 [1, 2, 3, 5]
 ```

 **[12-switch.py](12-switch.py)** - Switches the values of `a` and `b`.
 * Program must be 5 lines long
 ```
 vagrant:0x03-python-data_structures$ ./12-switch.py
 a=10 - b=89
 ```

 **[13-is_palindrome.c](13-is_palindrome.c)** - Determines of the Linked list given is a palindrome.
 ```
 vagrant:0x03-python-data_structures$ ./palindrome
 1
 17
 972
 50
 98
 98
 50
 972
 17
 1
 Linked list is a palindrome
 ```

 **[lists.h](lists.h)** - The header file for 13-is_palindrome

 2021 - All programs written by itsmuriuki