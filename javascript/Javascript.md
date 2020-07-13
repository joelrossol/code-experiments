# Javascript

## 1. Variables

Basic javascript would have you declare a variable with the 'var' keyword.  But modern practices would prefer you use 'const myVar = "foo"' or 'let myVar=';

```javascript
let myVar = foo;
const myVar = "value";
```



## 2. Math & Numbers

Basic arethmatic operators work as expected... +/-/* etc.  So Sum = A + B + C.  The remainder operator % will provide the remainder of a division of numbers.  The % operator will return 1/0 if the remainder is odd/even.

math.round(valueToRound)

math.ceil();

math.floor();

math.random()

To take a string and convert it to a number... use parsInt(val);

Number(numString);





## 3. Strings

Use "quotes" around string values.  You can add strings together using the (+) operator.

Use .**length** to find the length of a string or an array.  You can also use the bracket notation[3] to get a character in a string, similar to an array.

Cases:

.toUpperCase();

.toLowerCase();

Using the "slice"

var someChars = cityToCheck.slice(2, 5);

#### Looking up values in strings.

The '.indexOf()' or .lastIndexOf() methods.

let firstChar = textString.indexOf("value to look for")

.charAt(4) // gets us the character at a certain numeric index.

text.replace("lookup phrase or word", "the NEW value");

to globally replace, use ''/'' instead of quotation marks liks so:  text.replace(/phrase/g, "the new value")



### 4. Arrays

You can initialize an array with the bracket notation [];

You can store arrays within arrays by separating them with commas.

```javascript
var myNestArray = [["Joel", 37], ["Mark", 32]];

//Access values using nested []'s
myNestArray[0][1] = 37;
```



## 5. Objects {}

You can initialize an object using the following {} notation:

```javascript
var car = {
  make: "Ford",
  cylinders: 6,
  model: "mustang"
};

//access values using the [] notation.
console.log(car[make]);
```

### Checking if a property exists.

We have multiple ways to do this.

```javascript
if (theObj.hasOwnProperty('theprop')) {
    // take action
}
if (typeof theObj.prop !== 'undefined') {
  // take action
}
'fname' in theObj;     // => true
'lname' in theObj; // => false
```

More info available here: https://medium.com/@hohanga/how-to-check-if-a-property-exists-in-a-javascript-object-1e1f5f1323e9

https://dmitripavlutin.com/check-if-object-has-property-javascript/

#### Freeze Object

While part of the EX6 section as well, you can freeze an object using the Object.freeze(object) notation.



### 6. Functions

Declare a function with the 'function' keyword.

```javascript
function myFunct(arg){
	//execute
}
```

Variables stored within functions are limited to the function scope.  But variables stored outside the function are available/changable by the function.  If a variable of the same name is declared within the function, that variable will be used instead of the global one.



## 7. Loops & Iterators

##### FOR loop:

```javascript
for(let i = 0; i < var.length; i++){
	//do things
}
```

##### WHILE Loop:

```javascript
let i = 0;
while (i < 0) {
  //take action
i++;
}
```

##### DO-WHILE Loop

```javascript
let i = 0;
do {
	//take action
  i++;
} while (i < 10);
```



#### SWITCH statements

```
switch(val) {
  case 100:
  case 1000:
  case 10000:
    result = "even rounding";
    break;
  case 72:
    result = "4 alone";
}
```









## MISC.... need to edit

#Everything I've learned about Javascript

##Strings


In ES6, we can use template literals to print out variables in strings:

```
`${firstName} is my first name.`
'Michael is my first name.'
```

##Variables

Variables can be assigned a number of ways, but the best way is to use the 'let' keyword.

```
let quantity=200;
```

Using 'let' prevents variables from being over-written and is important for _____ coding standard, meaning, that immunability.

Variables can be functions, arrays, or objects.

```
let quantity = sumValue(){}
let ingredients = [value, value2, value3];
let scores =
```

#arrays


```
//converts a text string into an array
String.split(",");

//get a portion of an array
array.slice(1);
a.sort()
a.reverse()
a.push()
a.pop()


```


##Console Commands

console.log();


##unctions


##Methods
A method is a particular kind of function, one attached to an object and invoked using the dot notation.

```
String.includes('word');
string.length;
```


##Dates

let now = new Date();
now.getFullYear();    // This is what we want instead.
now.getMonth();
now.getDay();

##Regular Expressions

##objects

//basic treatment
let myObject ={}
myOjbect["firstName"] = "Joel";
myOjbect.fistname > Joel