# ===============================================================
# Function
# ===============================================================
# Function W/O  Parameter
def greet():
    print("Hello Frank")
    print("How are you doing Frank?")
    print("Hope, You're doing well.")

greet()

# # Simple Function that packages code into a named block
# def greet():
#     print("Hello Angela")
#     print("How do you do Jack Bauer?")
#     print("Isn't the weather nice?")


# greet()


# Function that allows for inputs
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Billie")



"""
Previously, we've seen that functions allow us to package code into a named block which can be used repeatedly at a later point.

PAUSE 1 - Review
Create a function called greet().
Write 3 print statements inside the function.
Call the greet() function and run your code.
Inputs
By adding a variable name inside the parentheses when we create (define) a new function, it allows that function to take inputs when called.

That means we can modify how the function behaves each time by passing in different inputs.

# Creating the function
def myFunction(input):
    print(f"Hey! {input}")
# Using the function
myFunction("Tommy") 
# Will output "Hey! Tommy"
Inputs are Variables
When you create a function with inputs, you are defining a variable name that will be given to the data that is passed in.

The name of the input variable, e.g. name in this code here: def greet(name): is called the parameter.

The value of the value of the input variable, e.g. Angela when you call the previous greet function: greet("Angela") is called the argument.
"""
# ===============================================================
# Parameter and Arguments
# ===============================================================
# Function with Parameter
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you doing {name}")

greet_with_name("Frank")

# def my_function(something):
#     Do this with somthing
#     Then do this
#     Finally do this
#
# my_function(123)

# Parameter - name, something
# Argument - "Frank", 123

# ===============================================================
# Positional vs. Keybord argument
# ===============================================================
# Function with more than one input
# Positional vs. Keyboard Argument
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Frank", "India")


# Positional Arugments
def positional_arguments(a,b,c):
    print(f"The first argument \"a\" is: {a}")
    print(f"The second argument \"b\" is: {b}")
    print(f"The Third argument \"c\" is: {c}")

positional_arguments(1, 2, 3)

# Keyword Arguments
def keyword_arguments(a,b,c):
    print(f"The first argument \"a\" is: {a}")
    print(f"The second argument \"b\" is: {b}")
    print(f"The Third argument \"c\" is: {c}")


keyword_arguments(a=1, b=2, c=3)

def greet_with_keyword_arguments(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with_keyword_arguments(location = "India", name = "Frank", )

"""
Multiple Inputs
You can have multiple inputs in functions. All you need to do is separate them with a comma ,.

PAUSE 1
Create a function with multiple inputs

 Hint 1 
PAUSE 2
Modify the function so that it prints the expected values.

def greet_with(name, location)
    Hello name
    What is it like in location
Positional Arguments
By default, when you create a function in Python, it will keep the order of arguments in the function definition.

e.g. In the function below, the first argument that goes in will always be printed before the second one. a = 2, b = 1

def my_function(a, b)
  print(a)
  print(b)
  
 my_function(2, 1)
 #It will print:
 # 2
 # 1
Keyword Arguments
You can use keywords when you provide the arguments when you call a function so that there is less confusion which value is assigned to which input parameter.

PAUSE 3
Call the greet_with() function using keyword arguments.

 Hint 2 
greet_with(location="London", name="Angela")
"""

# ===============================================================
# Life in weeks
# ===============================================================
def life_in_weeks(age):
    years_left = 90 - age
    weeks_left = years_left * 52
    print(f"You have {weeks_left} weeks left.")
    
life_in_weeks(24)

# ===============================================================
# Love calculator
# ===============================================================
def calculate_love_score(name1, name2):
    true_count = 0
    love_count = 0
    name = (name1 + name2).lower()
    true = "true"
    love = "love"
   
    for char in name:
        if char in true:
            true_count += 1
        else:
            true_count
    
    for char in name:
        if char in love:
            love_count += 1 
        else:
            love_count

    print(f"{true_count}{love_count}")
    # true_count = str(true_count)
    # love_count = str(love_count)
    # count = true_count + love_count
    
    # print(count)
calculate_love_score("Frank", "Angela")

# ===============================================================
# Optimised version of Love calculator
# ===============================================================
def calculate_love_score(boy_name, girl_name):
    combined_name = (boy_name + girl_name).lower()

    true_score = sum(combined_name.count(letter) for letter in "true")
    love_score = sum(combined_name.count(letter) for letter in "love")

    love_percentage = int(f"{true_score}{love_score}")

    print(f"Love Score: {love_percentage}")


boy_name = input("Enter the boy's name: ")
girl_name = input("Enter the girl's name: ")

calculate_love_score(boy_name, girl_name)