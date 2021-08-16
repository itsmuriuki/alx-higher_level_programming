# 0x09. Python - Everything is object

## Overview
This project focused on the object oriented programming paradigm in that everything in Python was an object. We learned about how all variable references are actually instances of a data type class. Additionally, we learned the difference between immutable and mutable objects and aliasing as well as how Python passes variables to functions.

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

### Text Files
* Only one line
* No shebang
* All files should end with new line
* All files should contain the answer to the question

## Tasks
### Mandatory
The mandatory tasks consisted of several scripts and questions with `Yes`, `No`, `True`, `False`, or other one word or data type answers. These answers are found in the text files in this repository. There was only one script in the mandatory section of this project.

All questions focused on using `a is b` or `a == b` to check if two objects were the same and if they shared the same value. Additionally, some questions asked whether the value of a specific variable would change based on their immutable or mutable nature and the operations applied to them.

The only script is as follows:
**[19-copy_list.py](19-copy_list.py)** - Returns a copy of a list
* Input list contains any type of objects
* Maximum of three lines
* no imported module
```
vagrant:0x09-python-everything_is_object$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
```
### Advanced
This part of the project also consisted of a section with the same format and text file answers as the previous section. These were additional "brain teasers" about how objects worked in Python.

I did one of the advanced scripts and it is below:
**[100-magic_string.py](100-magic_string.py)** - Returns a string n times the number of the iteration
* Maximum of four lines
* no imported module
```
vagrant:0x09-python-everything_is_object$ ./100-main.py
DHK
DHK, DHK
DHK, DHK, DHK
DHK, DHK, DHK, DHK
DHK, DHK, DHK, DHK, DHK
DHK, DHK, DHK, DHK, DHK, DHK
DHK, DHK, DHK, DHK, DHK, DHK, DHK
DHK, DHK, DHK, DHK, DHK, DHK, DHK, DHK
DHK, DHK, DHK, DHK, DHK, DHK, DHK, DHK, DHK
DHK, DHK, DHK, DHK, DHK, DHK, DHK, DHK, DHK, DHK
```
2021 - All programs written by itsmuriuki