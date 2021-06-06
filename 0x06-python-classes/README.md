# 0x06. Python - Classes and Objects

## Overview
This project was an introduction to Object Oriented Programming (OOP). It talks about what a class is, what an object and instance are, what are the differences between those, what are attributes, what are the differences between public, protected, and private attributes, the `self` keyword, methods, `__init__` method, data abstraction, data encapsulation, and information hiding, properties, and getters/setters.

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
**[0-square.py](0-square.py)** - Empty class `Square` that defines a squre
```
vagrant:0x06-python-classes$ ./0-main.py
<class '0-square.Square'>
{}
```

**[1-square.py](1-square.py)** - Adds instantiation function for a size attribute
* no imported module
```
vagrant:0x06-python-classes$ ./1-main.py
<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
```

**[2-square.py](2-square.py)** - Adds type/value verification to the instantiation function
```
vagrant:0x06-python-classes$ ./2-main.py
<class '2-square.Square'>
{'_Square__size': 3}
<class '2-square.Square'>
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0
```

**[3-square.py](3-square.py)** - Adds an area function to the class
```
vagrant:0x06-python-classes$ ./3-main.py
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
```

**[4-square.py](4-square.py)** - Adds getter and setter for the size attribute
```
vagrant:0x06-python-classes$ ./4-main.py
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
```

**[5-square.py](5-square.py)** - Adds a print function to print the square using hash signs
```
vagrant:0x06-python-classes$ ./5-main.py
###
###
###
--
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
--

--
```

**[6-square.py](6-square.py)** - Adds a position attribute to the class and prints accordingly
```
vagrant:0x06-python-classes$ ./6-main.py
###
###
###
--
###
###
###
--
###
###
###
--
```

### Advanced
**[100-singly_linked_list.py](100-singly_linked_list.py)** - Creates a singly linked list class and a node class. The singly linked list class has functions to add nodes to the list and print the list
```
vagrant:0x06-python-classes$ ./100-main.py
-4
-3
1
2
3
3
4
5
5
10
12
```

**[101-square.py](101-square.py)** - Adds functionality to the `Square` class that allows printing of an instance to have the same behavior as that of the print function in that class
```
vagrant:0x06-python-classes$ ./101-main.py
#####
#####
#####
#####
#####
--

#####
#####
#####
#####
#####
```

2021 - All programs written by itsmuriuki