# Procedural Programming (POP) vs. Object-Oriented Programming (OOP)

"""
Pillars of OOP
Encapsulation: Bundling data and methods into units to protect internal state.
Inheritance: Enabling classes to acquire properties from others for code reuse.
Polymorphism: Allowing methods to perform different functions based on the object.
Abstraction: Hiding complex implementation details to expose only essential functionality.
"""
# ===============================================================
# OOPS Concepts
# ===============================================================

# import another_module
# # print(another_module.another_variable)
#
# from turtle import Turtle, Screen
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
"""

# timmy = Turtle()
# print(timmy)

"""
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
# # object.method
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
#
# # object.attribute
# my_screen.exitonclick()

# ===============================================================
# importing external module
# ===============================================================

from prettytable import PrettyTable
# ClassName - "PascalCase"
# object = Class()
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)







