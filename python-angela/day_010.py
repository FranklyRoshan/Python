# ===============================================================
# Function with outputs
# ===============================================================

def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    full_name = f"{formatted_f_name} {formatted_l_name}"
    return full_name

# print(format_name("angela", "yu"))
formatted_name = format_name("aNgeLA", "yu")
print(formatted_name)

"""
We've seen functions with only an execution body, functions with inputs that allow for variation in execution of the function body and now we'll see the final form of functions. Functions that can have outputs.

PAUSE 1
Create a function called format_name() that takes two inputs: f_name and `l_name'.

PAUSE 2
Use the title() function to modify the f_name and l_name parameters into Title Case.

Syntax
You can create a function with a body, input and output like this:

def function_name(input_parameter):
    <body of function that uses input_argument>
    return output
Print vs. Output
Return vs. Display: The return statement is used to give back a value from a function, which can be used later, while print is used to display a value to the console only for the programmer to see.
"""

# ===============================================================
# Print vs. Return Output
# ===============================================================

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)

# ===============================================================
# Multiple return values
# ===============================================================

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

output = format_name(input("What is your first name?"), input("What is your last name?"))
print(output)

# Assiging a variable name to a function
rename = format_name
print(rename("AnGleA", "YU"))


"""
Functions terminate at the return keyword. If you write code below the return statement that code will not be executed.

However, you can have multiple return statements in one function. So how does that work?

Conditional Returns
When we have control flow, as in the code will behave differently (go down different execution paths) depending on certain conditional checks, we can end up with multiple endings (returns).

e.g.

def canBuyAlcohol(age):
    if age >= 18:
        return True
    else:
        return False
Empty Returns
You can also write return without anything afterwards, and this just tells the function to exit.

e.g.

def canBuyAlcohol(age):
    # If the data type of the age input is not a int, then exit.
    if type(age) != int:
        return

    if age >= 18:
        return True
    else:
        return False
"""

# ===============================================================
# Leap year
# ===============================================================

def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
is_leap_year(2000)

# ===============================================================
# Optimized version for Beginner - Leap year
# ===============================================================
def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

# ===============================================================
# Optimized Version - Leap year
# ===============================================================
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# ===============================================================
# Docstring
# ===============================================================
""" Docstrings in Python are string literals that appear as the first statement in a module, 
function, class, or method definition.  They serve as documentation, providing a clear 
explanation of what the code does, its parameters, return values, and usage examples. 

Syntax: Written using triple quotes (\""" or ''') immediately after the definition.

Accessibility: Accessible via the __doc__ attribute or the help() function.

Purpose: Multiline comments. Unlike comments (#), docstrings are retained at runtime and
are used to generate automated documentation (e.g., with Sphinx, Pydoc, or doctest).
"""

def format_name(f_name, l_name):
    """Take a first and last name then format it to return the
    title case version of the name"""
    
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)


"""
You can use docstrings to write multiline comments that document your code.

Syntax
Just enclose your text inside a pair of three double quotes.

e.g.

\""" 
My 
Multiline 
Comment 
\"""

Documenting Functions
A neat feature of docstrings is you can use it just below the definition of a function and that text will be displayed when you hover over a function call. It's a good way to remind yourself what a self-created function does.

e.g.

def my_function(num):
    \"""Multiplies a number by itself.\"""
    return num * num
"""

#=====================================================================
# Calculator Code
#=====================================================================
import calculator_art

print(calculator_art.logo)

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()

"""
The goal is to build a calculator program.

Demo
https://appbrewery.github.io/python-day10-demo/

Storing Functions as a Variable Value
You can store a reference to a function as a value to a variable. e.g.

def add(n1, n2):
    return n1 + n2
    
    
my_favourite_calculation = add
my_favourite_calculation(3, 5)  # Will return 8
In the starting file, you'll see a dictionary that references each of the mathematical calculations that can be performed by our calculator. Try it out and see if you can get it to perform addition, subtraction, multiplication and division.

PAUSE 1
TODO: Write out the other 3 functions - subtract, multiply and divide.

PAUSE 2
TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

PAUSE 3
TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.

Functionality
Program asks the user to type the first number.
Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
Program asks the user to type the second number.
Program works out the result based on the chosen mathematical operator.
Program asks if the user wants to continue working with the previous result.
If yes, program loops to use the previous result as the first number and then repeats the calculation process.
If no, program asks the user for the fist number again and wipes all memory of previous calculations.
Add the logo from art.py

Hint 1 
Try writing out a flowchart to plan your program.

 Hint 2 
To call multiplication from the operations dictionary, you would write your code like this:
result = operations["*"](n1= 5, n2= 3)

result would then be equal to 15.
"""




