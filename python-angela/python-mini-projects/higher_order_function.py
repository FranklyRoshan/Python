# ===============================================================
# Higher Order Function
# ===============================================================

def function_a(something):
    # Do this with "Something"
    # Then do this
    # Finally do this
    pass

def function_b():
    # Do this
    pass

# Higher Order Function
function_a(function_b)

# ===============================================================
# Example for Higher Order Function
# ===============================================================
# Calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Higher Order Function
def calculator(n1, n2, func):
    return func(n1, n2)

# Positional Arguments
result = calculator(2, 5, add)

# Keyword Arguments
# result = calculator(n1=2, n2=5, func=add)

print(result)

# ===============================================================
# Higher Order Function & Event Listeners
# ===============================================================

from  turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# Function
def move_forwards():
    tim.forward(10)

screen.listen()
# Event Listeners - onkey
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()