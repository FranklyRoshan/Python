"""The turtle module in Python is a built-in library that provides a virtual drawing board where a cursor, called a
"turtle," draws lines and shapes based on simple commands. It is a popular tool for beginners to learn fundamental
programming concepts like loops, functions, and coordinates through immediate, visual feedback."""

# # import another_module
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

from prettytable import PrettyTable
# ClassName - "PascalCase"
# object = Class()
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

print("apple")

