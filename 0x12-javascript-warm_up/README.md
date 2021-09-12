# 0x12. Javascript - Warmup

## Overview
The objective of this project was to understand and work with Javascript. This includes how to run a Javascript script, how to create variables and constants, the use of `var` vs `const` vs `let`, all the data types in Javascript, conditionals, loops, `break` and `continue` statements, objects, operators, `return` statement, conditional operators, dictionaries, and how to import files.

## Requirements
* All your files will be interpreted on `Ubuntu 14.04 LTS` using `node` (version 6.10.2)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/node`
* Your code should be `semistandard` compliant (version 11.0.0). Rules of Standard + semicolons on top.
* All your files must be executable
* Not allowed to use `var` to declare variables

## Tasks
### Mandatory
**[0-javascript_is_amazing.js](0-javascript_is_amazing.js)** - Script prints "Javascript is amazing"
```
$ ./0-javascript_is_amazing.js 
Javascript is amazing
```

**[1-multi_languages.js](1-multi_languages.js)** - Prints 3 lines on separate lines using `console.log()`
```
$ ./1-multi_languages.js 
C is fun
Python is cool
Javascript is amazing
```

**[2-arguments.js](2-arguments.js)** - Prints a message depending on the number of arguments passed. See the example below
```
$ ./2-arguments.js 
No argument
$ ./2-arguments.js DHK
Argument found
$ ./2-arguments.js DHK School
Arguments found
```

**[3-value_argument.js](3-value_argument.js)** - Prints the first argument that is passed to it in the command line. We were not allowed to use `length`
```
$ ./3-value_argument.js 
No argument
$ ./3-value_argument.js DHK
DHK
```

**[4-concat.js](4-concat.js)** - Takes the first two arguments supplied to the program and creates a sentence with the word 'is' in between the two arguments
```
$ ./4-concat.js c cool
c is cool
$ ./4-concat.js c 
c is undefined
$ ./4-concat.js
undefined is undefined
```

**[5-to_integer.js](5-to_integer.js)** - Converts an argument into an integer and displays it in the console output. We were not allowed to use `try/catch`
```
$ ./5-to_integer.js 
Not a number
$ ./5-to_integer.js 89
My number: 89
$ ./5-to_integer.js "89"
My number: 89
$ ./5-to_integer.js 89.89
My number: 89
$ ./5-to_integer.js DHK
Not a number
```

**[6-multi_languages_loop.js](6-multi_languages_loop.js)** - Prints three lines, similar to [1-multi_languages.js](1-multi_languages.js) except using an array of strings in a loop
```
$ ./6-multi_languages_loop.js 
C is fun
Python is cool
Javascript is amazing
```

**[7-multi_c.js](7-multi_c.js)** - Prints the string 'C is fun' x number of times to be determined by the user as an argument in the command line
```
$ ./7-multi_c.js 2
C is fun
C is fun
$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
$ ./7-multi_c.js 
Missing number of occurrences
```

**[8-square.js](8-square.js)** - Takes a size provided to it on the command line and prints a square of that size with the character 'X'
```
$ ./8-square.js
Missing size
$ ./8-square.js DHK
Missing size
$ ./8-square.js 2
XX
XX
$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
```

**[9-add.js](9-add.js)** - Prints the addition of 2 integers as a function called `add`
```
$ ./9-add.js 
NaN
$ ./9-add.js 1
NaN
$ ./9-add.js 1 7
8
$ ./9-add.js 13 89
102
```

**[10-factorial.js](10-factorial.js)** - Prints the factorial of a number specified by the user using a recursive function
```
$ ./10-factorial.js 
1
$ ./10-factorial.js 3
6
$ ./10-factorial.js 89
1.6507955160908452e+136
$ ./10-factorial.js 333
Infinity
```

**[11-second_biggest.js](11-second_biggest.js)** - Prints the second biggest integer in a list of integers entered by the user on the command line
```
$ ./11-second_biggest.js 
0
$ ./11-second_biggest.js 1
0
$ ./11-second_biggest.js 4 2 5 3 0 -3
4
```

**[12-object.js](12-object.js)** - Updates the following script to replace the value of the object from `12` to `89`
```
$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);
$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
```

**[13-add.js](13-add.js)** - Returns the addition of 2 integers from a module that is imported like in the following example
```
$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
$ ./13-main.js
8
```

### Advanced
**[100-let_me_const.js](100-let_me_const.js)** - Imported module that modifies the value of `myVar` below from `89` to `333`
```
$ cat 100-main.js
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
$ ./100-main.js
333
```

**[101-call_me_moby.js](101-call_me_moby.js)** - Executes a function inside of a function a set number of times. This function will be imported. See the example below
```
$ cat 101-main.js
#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
$ ./101-main.js
C is fun
C is fun
C is fun
```

**[102-add_me_maybe.js](102-add_me_maybe.js)** - Increments and calls a function from within another function. This function will be imported. See the example below
```
$ cat 102-main.js
#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
$ ./102-main.js
New value: 5
```

**[103-object_fct.js](103-object_fct.js)** - Adds a new function `incr` to an object that increments the `value` attribute of the object. See the example below
```
$ cat 103-object_fct.js
#!/usr/bin/node
let myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
$ ./103-object_fct.js 
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }
```

2021 - All programs written by @itsmuriuki