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
