# 0x13. Javascript - Objects, Scopes, and Closures

## Overview
The objective of this project was to understand object-oriented Javascript and understanding how to create objects, how to use the word `this`, what `undefined` means, variable scope, closures, prototypes, and inheritance.

## Requirements
* All your files will be interpreted on `Ubuntu 14.04 LTS` using `node` (version 6.10.2)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/node`
* Your code should be `semistandard` compliant (version 11.0.0). Rules of Standard + semicolons on top.
* All your files must be executable
* Not allowed to use `var` to declare variables

## Tasks
### Mandatory
**[0-rectangle.js](0-rectangle.js)** - An empty Rectangle class that defines a rectangle using the `class` notation
```
$ cat 0-main.js
#!/usr/bin/node
const Rectangle = require('./0-rectangle');

const r1 = new Rectangle();
console.log(r1);
console.log(r1.constructor);
$ ./0-main.js
Rectangle {}
[Function: Rectangle]
```

**[1-rectangle.js](1-rectangle.js)** - Adds a constructor with a width and height argument into the class definition
```
$ cat 1-main.js
#!/usr/bin/node
const Rectangle = require('./1-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

$ ./1-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle { width: 2, height: -3 }
2
-3
Rectangle { width: 2, height: undefined }
2
undefined
```

**[2-rectangle.js](2-rectangle.js)** - Adds a condition that if both the width and height are 0 or negative, an empty object is created
```
$ cat 2-main.js
#!/usr/bin/node
const Rectangle = require('./2-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

const r4 = new Rectangle(2, 0);
console.log(r4);
console.log(r4.width);
console.log(r4.height);

$ ./2-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
```

**[3-rectangle.js](3-rectangle.js)** - Adds a print() function to the rectangle class which prints the rectangle using the character `X`
```
$ cat 3-main.js
#!/usr/bin/node
const Rectangle = require('./3-rectangle');

const r1 = new Rectangle(2, 3);
r1.print();

const r2 = new Rectangle(10, 5);
r2.print();

$ ./3-main.js
XX
XX
XX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
```

**[4-rectangle.js](4-rectangle.js)** - Adds a method rotate() and double() which exchange the width and height and which multiplies the width and height by 2, respectively
```
$ cat 4-main.js
#!/usr/bin/node
const Rectangle = require('./4-rectangle');

const r1 = new Rectangle(2, 3);
console.log('Normal:');
r1.print();

console.log('Double:');
r1.double();
r1.print();

console.log('Rotate:');
r1.rotate();
r1.print();

$ ./4-main.js
Normal:
XX
XX
XX
Double:
XXXX
XXXX
XXXX
XXXX
XXXX
XXXX
Rotate:
XXXXXX
XXXXXX
XXXXXX
XXXXXX
```

**[5-square.js](5-square.js)** - Creates a Square class which inherits from the Rectangle class in `4-rectangle.js`. The constructor is called using `super()`
```
$ cat 5-main.js
#!/usr/bin/node
const Square = require('./5-square');

const s1 = new Square(4);
s1.print();
s1.double();
s1.print();

$ ./5-main.js
XXXX
XXXX
XXXX
XXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
```

**[6-square.js](6-square.js)** - Adds an instance method charPrint(c) which prints the rectangle using the character c. If c is undefined, it prints the rectangle using the character `X`
```
$ cat 6-main.js
#!/usr/bin/node
const Square = require('./6-square');

const s1 = new Square(4);
s1.charPrint();

s1.charPrint('C');

$ ./6-main.js
XXXX
XXXX
XXXX
XXXX
CCCC
CCCC
CCCC
CCCC
```

**[7-occurrences.js](7-occurrences.js)** - Prints the number of occurrences of a specific element in a given list
```
$ cat 7-main.js
#!/usr/bin/node
const nbOccurences = require('./7-occurrences').nbOccurences;

console.log(nbOccurences([1, 2, 3, 4, 5, 6], 3));
console.log(nbOccurences([3, 2, 3, 4, 5, 3, 3], 3));
console.log(nbOccurences(["H", 12, "c", "H", "DHK", 8], "H"));

$ ./7-main.js
1
4
2
```

**[8-esrever.js](8-esrever.js)** - Returns the reversed version of a list
```
$ cat 8-main.js
#!/usr/bin/node
const esrever = require('./8-esrever').esrever;

console.log(esrever([1, 2, 3, 4, 5]));
console.log(esrever(["DHK", 89, { id: 12 }, "String"]));

$ ./8-main.js
[ 5, 4, 3, 2, 1 ]
[ 'String', { id: 12 }, 89, 'DHK' ]
```

**[9-logme.js](9-logme.js)** - Prints the number of arguments already printed along with the new argument. The format is `<number of arguments printed>: <current argument value>`
```
$ cat 9-main.js
#!/usr/bin/node
const logMe = require('./9-logme').logMe;

logMe("Hello");
logMe("DHK");
logMe("School");

$ ./9-main.js
0: Hello
1: DHK
2: School
```

**[10-converter.js](10-converter.js)** - Converts a number from base 10 to another base passed as an argument. No imports of any file or new variables were allowed
```
$ cat 10-main.js
#!/usr/bin/node
const converter = require('./10-converter').converter;

let myConverter = converter(10);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));


myConverter = converter(16);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));

$ ./10-main.js
2
12
89
2
c
59
```

2021- All programs written by itsmuriuki
