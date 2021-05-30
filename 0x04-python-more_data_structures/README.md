# 0x04. Python - More Data Structures: Set, Dictionary

## Overview
This project concerns additional data structures such as sets and dictionaries. The programs written here deal with sets and their methods, dictionaries and their methods, sets vs lists, dictionaries vs sets and lists, iterating through a dictionary and set, dictionary keys and values, the lambda function, the map function, and the reduce function.

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
**[0-square_matrix_simple.py](0-square_matrix_simple.py)** - Computes the square value of all integers of a matrix
* matrix is a 2D array
* Initial matrix should not be modified
* no imported modules
```
vagrant:0x04-python-more_data_structures$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

**[1-search_replace.py](1-search_replace.py)** - Replaces all occurrences of an element by another in a new list
* no imported module
```
vagrant:0x04-python-more_data_structures$ ./1-main.py
[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
```

**[2-uniq_add.py](2-uniq_add.py)** - Adds all unique integers in a list
* no imported module
```
vagrant:0x04-python-more_data_structures$ ./2-main.py
Result: 15
```

**[3-common_elements.py](3-common_elements.py)** - Returns a set of common elements in two sets
* no imported module
```
vagrant:0x04-python-more_data_structures$ ./3-main.py
['C']
```

**[4-only_diff_elements.py](4-only_diff_elements.py)** - Returns a set of all elements present in only one set
* no imported modules
```
vagrant:0x04-python-more_data_structures$ ./4-main.py
['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
```

**[5-number_keys.py](5-number_keys.py)** - Returns the number of keys in a dictionary
* no imported modules
```
vagrant:0x04-python-more_data_structures$ ./5-main.py
Number of keys: 3
```

**[6-print_sorted_dictionary.py](6-print_sorted_dictionary.py)** - Prints a dictionary by ordered keys
* Can assume all keys are strings
* Keys should be sorted in alphabetic order
* no imported modules
```
vagrant:0x04-python-more_data_structures$ ./6-main.py
Number: 89
ids: [1, 2, 3]
language: C
track: Low level
```

**[7-update_dictionary.py](7-update_dictionary.py)** - Replaces or adds key/value in a dictionary
* If key exists, value replaced
* If key does not exist, it is created
* no imported module
```
vagrant:0x04-python-more_data_structures$ ./7-main.py
language: Python
number: 89
track: Low level
--
language: Python
number: 89
track: Low level
--
--
city: San Francisco
language: Python
number: 89
track: Low level
--
city: San Francisco
language: Python
number: 89
track: Low level
```

**[8-simple_delete.py](8-simple_delete.py)** - Deletes a key in a dictionary
* if key does not exist, dictionary does not change
* no imported module
```
vagrant:0x04-python-more_data_structures$ ./8-main.py
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
--
--
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
```

**[9-multiply_by_2.py](9-multiply_by_2.py)** - Returns a new dictionary with all values multiplied by 2
* Returns new dictionary
* Assume all values are integers
* no imported module
```
vagrant:0x04-python-more_data_structures$ ./9-main.py
Alex: 8
Bob: 14
John: 12
Mike: 14
Molly: 16
--
Alex: 16
Bob: 28
John: 24
Mike: 28
Molly: 32
```

**[10-best_score.py](10-best_score.py)** - Returns a key with the bigger integer value
* Assume all values are integers
* If no score found, return `None`
* Assume all scores different
* no imported module
```
vagrant:0x04-python-more_data_structures$ ./10-main.py
Best score: Molly
Best score: None
```

**[11-mutiply_list_map.py](11-mutiply_list_map.py)** - Returns a list with all values multiplied by a number without using loops
* Must use `map()`
* No imported module
* Max 3 lines
```
vagrant:0x04-python-more_data_structures$ ./11-main.py
[4, 8, 12, 16, 24]
[1, 2, 3, 4, 6]
```

**[12-roman_to_int.py](12-roman_to_int.py)** - Converts a roman numeral to decimal number
```
vagrant:0x04-python-more_data_structures$ ./12-main.py
X = 10
VII = 7
IX = 9
LXXXVII = 87
DCCVII = 707
CM = 900
I = 1
CX = 110
MCMLXXXIV = 1984
```

### Advanced
**[100-weight_average.py](100-weight_average.py)** - Function returns the weighted average of all integers in the tuple
* no imported module
```
vagrant:0x04-python-more_data_structures$ ./100-main.py
Average: 2.80
```

**[102-complex_delete.py](102-complex_delete.py)** - Deletes keys with a specific value in a dictionary
* no imported module
* if value does not exist, dictionary does not change
* All keys with this value have to be deleted
```
vagrant:0x04-python-more_data_structures$ ./102-main.py
ids: [1, 2, 3]
track: Low
--
ids: [1, 2, 3]
track: Low
--
--
ids: [1, 2, 3]
track: Low
--
ids: [1, 2, 3]
track: Low
```

2021 - All programs written by itsmuriuki