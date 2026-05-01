# from turtle import Turtle, Screen
import turtle as t
import random

# ===============================================================
# Python Turtle
# ===============================================================
# tim = t.Turtle()
# tim.shape("turtle")
# tim.color("coral")

# screen = t.Screen()
# screen.exitonclick()

# ===============================================================
# Draw a Square
# ===============================================================
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# screen = t.Screen()
# screen.exitonclick()

# ===============================================================
# Draw a Dashed Line
# ===============================================================
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#
# screen = t.Screen()
# screen.exitonclick()

# ===============================================================
# Draw Different Shapes
# ===============================================================
# colors = ["CornFlowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "Coral", "Wheat", "StateGray", "SeaGreen"]
# num_sides = 3
# length = 100
#
# def draw_shape():
#     global num_sides
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(length)
#         tim.right(angle)
#
# for i in range (0,10):
#     tim.color(random.choice(colors))
#     num_sides += i
#     draw_shape()
#
# screen = t.Screen()
# screen.exitonclick()

# ===============================================================
# Generate Random Walk - Python Tuples and generate random RGB Colors
# ===============================================================
# tim = t.Turtle()
# t.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0,255)
#     random_color = (r,g,b)
#     return random_color
#
#
# directions = [0, 90, 180, 270]
# tim.width(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#
# screen = t.Screen()
# screen.exitonclick()

# ===============================================================
# Draw a Spirograph
# ===============================================================
tim = t.Turtle()
t.colormode(255)

tim.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range (int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(3)

screen = t.Screen()
screen.exitonclick()




