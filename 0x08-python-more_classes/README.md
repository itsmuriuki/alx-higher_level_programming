# 0x08. Python - More Classes and Objects

## Overview
This project delves farther into the world of OOP and classes/objects

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
**[0-rectangle.py](0-rectangle.py)** - Empty `Rectangle` class that defines a rectangle
```
vagrant:0x08-python-more_classes$ ./0-main.py
<class '0-rectangle.Rectangle'>
{}
```

**[1-rectangle.py](1-rectangle.py)** - Adds setter and getter functions for the width and height attributes
```
vagrant:0x08-python-more_classes$ ./1-main.py
{'_Rectangle__height': 4, '_Rectangle__width': 2}
{'_Rectangle__height': 3, '_Rectangle__width': 10}
{'_Rectangle__height': 0, '_Rectangle__width': 0}
width must be an integer
height must be an integer
width must be an integer
__init__() takes from 1 to 3 positional arguments but 4 were given
width must be an integer
```

**[2-rectangle.py](2-rectangle.py)** - Adds functions to print the perimeter and area of the rectangle
```
vagrant:0x08-python-more_classes$ ./2-main.py
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
Area: 0 - Perimeter: 0
--
Area: 1000000 - Perimeter: 4000
--
width must be >= 0
--
Area: 0 - Perimeter: 0
--
```

**[3-rectangle.py](3-rectangle.py)** - Adds functionality for if the `print()` or `str()` functions are called with the rectangle
```
vagrant:0x08-python-more_classes$ ./3-main.py
Area: 8 - Perimeter: 12
##
##
##
##
<3-rectangle.Rectangle object at 0x7f5f75bdbeb8>
--
##########
##########
##########
<3-rectangle.Rectangle object at 0x7f5f75bdbeb8>
```

**[4-rectangle.py](4-rectangle.py)** - Adds functionality if `repr()` is called so that another rectangle can be created by using `eval()`
```
vagrant:0x08-python-more_classes$ ./4-main.py
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f8f9d2a5c88
--
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f8f9d2a5cc0
--
False
True
```

**[5-rectangle.py](5-rectangle.py)** - Adds functionality if `del` is called and a rectangle is deleted
```
vagrant:0x08-python-more_classes$ ./5-main.py
Area: 8 - Perimeter: 12
Bye rectangle...
[NameError] name 'my_rectangle' is not defined
```

**[6-rectangle.py](6-rectangle.py)** - Adds functionality to keep a class attribute that keeps track of the number of instances of the rectangle present
```
vagrant:0x08-python-more_classes$ ./6-main.py
6 instances of Rectangle
Bye rectangle...
5 instances of Rectangle
Bye rectangle...
4 instances of Rectangle
Bye rectangle...
3 instances of Rectangle
Bye rectangle...
2 instances of Rectangle
Bye rectangle...
1 instances of Rectangle
Bye rectangle...
0 instances of Rectangle
```

**[7-rectangle.py](7-rectangle.py)** - Adds functionality to change the print symbol
```
vagrant:0x08-python-more_classes$ ./7-main.py
########
########
########
########
--
&&&&&&&&
&&&&&&&&
&&&&&&&&
&&&&&&&&
--
##
--
CC
--
CCCCCCC
CCCCCCC
CCCCCCC
```

**[8-rectangle.py](8-rectangle.py)** - Adds functionality to compare two rectangle instances
```
vagrant:0x08-python-more_classes$ ./8-main.py
my_rectangle_1 is bigger or equal to my_rectangle_2
my_rectangle_2 is bigger than my_rectangle_1
Bye rectangle...
Bye rectangle...
```

**[9-rectangle.py](9-rectangle.py)** - Adds functionality that allows the rectangle to create a square instance of the rectangle since a square is a rectangle
```
vagrant:0x08-python-more_classes$ ./9-main.py
Area: 25 - Perimeter: 20
#####
#####
#####
#####
#####
Bye rectangle...
```

2021 - All programs written by itsmuriuki