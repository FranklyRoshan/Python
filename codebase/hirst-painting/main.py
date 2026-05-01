# ===============================================================
# The Hirst Spot Painting Project Part 1 - Extracting RGB Color Values from image
# ===============================================================
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     # rgb_colors.append(color.rgb)
#
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
# ===============================================================
# The Hirst Spot Painting Project Part 2 - Drawing the dots
# ===============================================================

import turtle as turtle_module
import random

tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

rgb_colors = [(239, 229, 221), (220, 153, 95), (242, 222, 229), (35, 112, 152), (122, 170, 198), (202, 132, 157), (219, 235, 228), (212, 227, 237), (153, 65, 88), (198, 86, 112), (34, 132, 96), (212, 84, 65), (236, 200, 102), (160, 76, 57), (122, 182, 158), (160, 161, 49), (48, 168, 139), (235, 163, 182), (46, 160, 180), (242, 166, 154), (18, 94, 69), (145, 210, 220), (149, 214, 202), (46, 56, 99), (92, 46, 71), (66, 44, 64), (116, 112, 161), (177, 185, 218), (31, 56, 88), (16, 72, 47)]
len_rgb_colors = len(rgb_colors)

tim.setheading(225)
tim.forward(300)
tim.setheading(0)


for i in range (10):
    for _ in range (10):
        tim.dot(20, random.choice(rgb_colors))
        tim.forward(50)

    tim.setheading(90)
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)
    if i % 2 == 0:
        tim.setheading(180)
    else:
        tim.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()


