
# built-in-library
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



# another-module

another_variable = "Frank"



# another-module
"""Importing Module"""
# import turtle
# time = turtle.Turtle()

from turtle import Turtle
tim = Turtle()
tom = Turtle()
terry = Turtle()

# # Don't use this wild card import
# from turtle import *
# from random import *

"""Aliasing Module"""
import turtle as t
tracey = t.Turtle()

"""Installing Module"""
import heroes
print(heroes.gen())

# main.py
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("peachpuff")

for _ in range(4):
    tim.forward(100)
    tim.right(90)


screen = Screen()
screen.exitonclick()