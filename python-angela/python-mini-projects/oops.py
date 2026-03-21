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
# # object = Class()
# timmy = Turtle()
# print(timmy)
#
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







