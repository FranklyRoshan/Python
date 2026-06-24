# --- Python Operators ---
"""
Python Operators
Operators are used to perform operations on variables and values.

In the example below, we use the + operator to add together two values:
"""
print(10 + 5)
"""
Although the + operator is often used to add together two values, like in the example above, it can also be used to add together a variable and a value, or two variables:
"""

sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)

"""
Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
"""

# --- Arithmetic Operators ---
"""
Python Arithmetic Operators
Arithmetic Operators
Arithmetic operators are used with numeric values to perform common mathematical operations:

Operator	Name	Example	
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y
"""

"""
Examples
Here is an example using different arithmetic operators:
"""
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)


"""
Division in Python
Python has two division operators:

/ - Division (returns a float)
// - Floor division (returns an integer)
"""
"""
Example
Division always returns a float:
"""
x = 12
y = 5

print(x / y)


"""
Example
Floor division always returns an integer.

It rounds DOWN to the nearest integer:
"""

x = 12
y = 5

print(x / y)

# =-- Assignment Operators ---
"""
Python Assignment Operators
Assignment Operators
Assignment operators are used to assign values to variables:

Operator	Example	Same As	
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
:=	print(x := 3)	x = 3 print(x)
"""

"""
The Walrus Operator
Python 3.8 introduced the := operator, known as the "walrus operator". It assigns values to variables as part of a larger expression:
"""
"""
Example
The count variable is assigned in the if statement, and given the value 5:
"""
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

# --- Ternary Operator ---
"""
Python Ternary Operator
The Ternary Operator
The ternary operator allows you to assign one value if a condition is true, and another if it is false:
"""

"""
Example
Assign a value to x:

Assign the value "WEEKEND!" if the number is higher than 5, otherwise "Workday":
"""
num = 6

x = "WEEKEND!" if num > 5 else "Workday"

print(x)

# Note: The ternary operator is not an actual operator, it is a conditional expression, or a shorthand if statement.

"""
Instead of Elif:
The ternary operator can be used instead of elif in longer if statements:
"""

"""
Example
Assign:
- "Fri" if num is 5
- "Sat" if num is 6
- "Sun" if num is 7
- otherwise assign "weekday":
"""
num = 6

x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

print(x)


# --- Comparison Operators ---
"""
Python Comparison Operators
Comparison Operators
Comparison operators are used to compare two values:

Operator	Name	Example	Try it
==	Equal	x == y	
!=	Not equal	x != y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y
"""

"""
Examples
Comparison operators return True or False based on the comparison:
"""

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

"""
Chaining Comparison Operators
Python allows you to chain comparison operators:
"""
x = 5

print(1 < x < 10)

print(1 < x and x < 10)

# --- Logical Operators ---
"""
Python Logical Operators
Logical Operators
Logical operators are used to combine conditional statements:

Operator	Description	Example	Try it
and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
"""
"""
Examples
Example
Test if a number is greater than 0 and less than 10:
"""

x = 5

print(x > 0 and x < 10)

"""
Example
Test if a number is less than 5 or greater than 10:
"""

x = 5

print(x < 5 or x > 10)

"""
Example
Reverse the result with not:
"""
x = 5

print(not(x > 3 and x < 10))

# --- Identity Operators --- 
"""
Python Identity Operators
Identity Operators
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

Operator	Description	Example	
is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object
"""

"""
Example
The is operator returns True if both variables point to the same object:
"""
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

"""
Example
The is not operator returns True if both variables do not point to the same object:
"""
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)


"""
Difference Between is and ==
is - Checks if both variables point to the same object in memory
== - Checks if the values of both variables are equal
"""
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

# --- Membership Operators ---
"""
Python Membership Operators
Membership Operators
Membership operators are used to test if a sequence is presented in an object:

Operator	Description	Example	Try it
in 	Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object
"""
"""
Example
Check if "banana" is present in a list:
"""
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)


"""
Example
Check if "pineapple" is NOT present in a list:
"""
fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)


"""

Membership in Strings
The membership operators also work with strings:
"""
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

# --- Bitwise Operators ---
"""
Python Bitwise Operators
Bitwise Operators
Bitwise operators are used to compare (binary) numbers:

Operator	Name	Description	Example	
& 	AND	Sets each bit to 1 if both bits are 1	x & y	
|	OR	Sets each bit to 1 if one of two bits is 1	x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
~	NOT	Inverts all the bits	~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
"""


"""
Examples
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:
"""
print(6 & 3)
"""
The binary representation of 6 is 0110
The binary representation of 3 is 0011

Then the & operator compares the bits and returns 0010, which is 2 in decimal.
"""


"""
Example
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:
"""
print(6 | 3)
"""
The binary representation of 6 is 0110
The binary representation of 3 is 0011

Then the | operator compares the bits and returns 0111, which is 7 in decimal.
"""

"""
Example
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:
"""
print(6 ^ 3)
"""
The binary representation of 6 is 0110
The binary representation of 3 is 0011

Then the ^ operator compares the bits and returns 0101, which is 5 in decimal.
"""

# --- Operator Precedence ---
"""
Python Operator Precedence
Operator Precedence
Operator precedence describes the order in which operations are performed.
"""
"""
Example
Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
"""
print((6 + 3) - (6 + 3))

"""
Example
Multiplication * has higher precedence than addition +, and therefore multiplications are evaluated before additions:
"""
print(100 + 5 * 3)

"""
Precedence Order
The precedence order is described in the table below, starting with the highest precedence at the top:

Operator	Description	
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR
"""

"""
Left-to-Right Evaluation
If two operators have the same precedence, the expression is evaluated from left to right.
"""
"""
Example
Addition + and subtraction - has the same precedence, and therefore we evaluate the expression from left to right:
"""
print(5 + 4 - 7 + 3)

