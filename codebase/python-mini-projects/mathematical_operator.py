
# ===============================================================
# Mathematical Operations
# ===============================================================
def mathematical_operations():
    print("My age: " + str(12))

    name_of_the_user = input("Enter your name ")
    length_of_name = len(name_of_the_user)

    print(type("Number of letters in your name: ")) # str
    print(type(length_of_name)) # int

    print("Number of letters in your name: " + str(length_of_name))

    print(5 + 3)
    print(5 - 3)
    print(5 * 3)
    print(5 / 3)
    print(5 // 3)
    print(5 ** 3)

    # PEMDAS

    # ()
    # **
    # * OR /
    # + OR -

    print(3 * 3 + 3 / 3 - 3)
    print(3 * (3 + 3) / 3 - 3)
mathematical_operations()

"""
Basic Operators
Learn to use the basic mathematical operators, +, -, *, /, // and **

PEMDAS
Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

PAUSE 1. What is the output of this code?
print(3 * 3 + 3 / 3 - 3)

PAUSE 2. Change the code so it outputs 3?
print(3 * 3 + 3 / 3 - 3)
"""

# ===============================================================
# Number Manipulation
# ===============================================================
def number_manipulation():
    bmi = 84 / 1.65 ** 2

    print(bmi)
    print(int(bmi))
    print(round(bmi))
    print(round(bmi,2))

    score = 1

    # User scores a point
    score += 2
    print(score)

    # f-string
    score = 0
    height = 1.8
    You_are_winning = True


    print(f"Your score is = {score}, your height is {height}, You are winning is {You_are_winning}")
number_manipulation()

"""
Flooring a Number
You can floor a number or remove all decimal places using the int() function which converts a floating point number (with decimal places) into an integer (whole number).

int(3.738492) # Becomes 3

Rounding a Number
However, if you want to round a decimal number to the nearest whole number using the traditional mathematical way, where anything over .5 rounds up and anything below rounds down. Then you can use the python round() function.

round(3.738492) # Becomes 4

round(3.14159) # Becomes 3

round(3.14159, 2) # Becomes 3.14

Assignment Operators
Assignment operators such as the addition assignment operator += will add the number on the right to the original value of the variable on the left and assign the new value to the variable.

+=

-=

*=

/=

f-Strings
In Python, we can use f-strings to insert a variable or an expression into a string.

age = 12

print(f"I am {age} years old")

# Will output I am 12 years old.
"""
