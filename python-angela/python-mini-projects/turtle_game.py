# ===============================================================
# Turtle Race Game
# ===============================================================
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ").lower()
print(user_bet)

colors= ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_positions = [-70, -40, -10, 20, 50, 80, 110]
all_turtles = []

for turtle_index in range(0,7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        """
        All turtles by default have a height of 20px and width of 20px.
        All turtle positions are measured form their center
        """
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()

"""
Key Components of the Process

* Instantiation: This is the act of creating a unique "instance" (an object) from a class blueprint. In your example,
Turtle is the class (the blueprint), and tim is the specific instance (the individual turtle).
* Initialization: Immediately after the object is created, Python automatically runs the init() method to set the
object's starting state, such as its initial position and color.
* Constructor: The call Turtle() acts as a constructor, which is a special function that handles both the creation and
setup of the new object. [1, 2, 3, 4, 5]

Code  Role
Turtle  - The Class (the template for all turtles).
Turtle()  - The Constructor call that triggers instantiation.
timmy - The Instance or Object (the specific entity you can control).

====================================================================================================================

In the world of Object-Oriented Programming (OOP), these represent the two ways you interact with an object:
1. object.method() (The Action)
A method is a function that belongs to an object. It represents what the object can do.

* Syntax: Always followed by parentheses (), even if empty.
* Example: tim.forward(100) or tim.right(90).
* Purpose: To perform an operation or change the state of the object.

2. object.attribute (The Data)
An attribute is a variable that belongs to an object. It represents what the object is (its characteristics).

* Syntax: No parentheses.
* Example: tim.color or tim.pensize.
* Purpose: To store or retrieve information about the object's current state.

Feature         object.method()     object.attribute
Analogy         A Verb (Action)     A Noun (Trait)
Notation        Uses ()             No ()
Turtle Example  tim.pendown()       tim.heading
Result          Triggers behavior   Accesses data
"""