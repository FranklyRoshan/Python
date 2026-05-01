# ===============================================================
# Etch-A-Sketch App
# ===============================================================
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def forwards():
    tim.forward(10)

def backwards():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(forwards, "w")
screen.onkey(backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_drawing, "c")

screen.exitonclick()
