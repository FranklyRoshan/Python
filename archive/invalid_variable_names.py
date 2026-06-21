''' An invalid variable in Python refers to a variable name that does not adhere to Python's naming conventions and rules. Using such a name will result in a SyntaxError or NameError.
Here are the common reasons for an invalid variable name in Python: 
Starting with a Number: Variable names cannot begin with a digit. They must start with a letter (a-z, A-Z) or an underscore (_).
Python '''

    # Invalid
    1variable = 10 

''' Using Special Characters (other than underscore): Variable names can only contain letters, numbers, and underscores. Special characters like @, #, $, %, !, -, etc., are not allowed.
Python '''

    # Invalid
    my-variable = 20
    variable@name = 10

''' Python Identifiers (Variable Names)
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords. '''

# Example
# Illegal variable names:

2myvar = "John"
my-var = "John"
my var = "John"

# Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"