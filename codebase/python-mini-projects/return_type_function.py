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

