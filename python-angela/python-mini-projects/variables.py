# ===============================================================
# Print Statement
# ===============================================================
def printing():
    # Write your code below this line 👇
    print("Hello World!")
# Main method
printing()

# ===============================================================
# String Manipulation
# ===============================================================
def string_mainpulation():
    # Write your code below this line 👇
    # Escape sequence
    # \n (new line),\" (double quote), \' (single qoute), \t (tab),\b (backspace), 
    # Others include \r (carriage return, \f (form feed), along with octal (\oooo), hex (\xhh) and unicode (\uxxx), etc
    print("Hello world!\nHello world!\nHello world!")
    print("Hello " + "Angela!")
    print("Hello" + " Angela!")
    print("Hello" + " " + "Angela!")

    import time
    # Replace "Loading..." with complete
    print("Loading...", end="")
    time.sleep(1)
    print("\rComplete")

string_mainpulation()

# ===============================================================
# Input Function
# ===============================================================
def input_Function():
    # This line of code will take an input using the input() function
    # Comment code shortcut - "Ctrl + /"
    # To Select Whole line - "Ctrl + C"
    print("Hello " + input("What's your name? ") + "!")
    print(f"You're {int(input("How old are you? "))} years old.")
input_Function()

# ===============================================================
# Variables
# ===============================================================
def variables():
    name = "Jack"
    print(name)
    name = "Angela"
    print(name)
    print("Hello " + name + "!")

    
    first_name = input("What's your first name? ")
    last_name = input("What's your last name? ")

    name = first_name + " " + last_name
    print(name.title())
variables()

# ===============================================================
# Variable Naming
# ===============================================================
def variable_naming():
    # print(len(input("What is your name? ")))
    username = input("What is your name? ")
    length = len(username)
    print(length)


    name = "Angela"
    length = len(name)
    print(length)

    # Type conversion
    print("Length of your name is " + str(length))
    # Number Manipulation - f-string
    print(f"Length of your name is {length}")
variable_naming()

# ===============================================================
# Band Name Generator Project
# ===============================================================
def band_name_generator():
    print("Welcome to the Band Name Generator.")
    city = input("What's the name of the city you grew up in?\n")
    pet = input("What's your pet's name?\n")
    band_name = city + " " + pet
    print("Your band name could be " + band_name)
band_name_generator()

"""
Create a greeting for your program.
Ask the user for the city that they grew up in and store it in a variable.
Ask the user for the name of a pet and store it in a variable.
Combine the name of their city and pet and show them their band name.
 Hint 1 
Make sure the input cursor shows on a new line:
 Hint 2 
Demo:
Try it out first here
"""