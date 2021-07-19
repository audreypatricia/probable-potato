# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_color = []
#
# for color in colors:
#     rgb_color.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(rgb_color)

# color_list taken from color_gram
color_list = [(25, 108, 164), (194, 38, 81), (238, 161, 49), (234, 215, 85), (226, 237, 228), (223, 137, 176), (144, 108, 56), (102, 197, 219), (206, 166, 29), (20, 57, 132), (214, 73, 90), (239, 89, 50), (141, 208, 227), (118, 192, 140), (3, 186, 176), (106, 107, 199), (138, 29, 73), (4, 161, 86), (98, 51, 36), (22, 156, 210), (232, 165, 184), (175, 185, 221), (29, 90, 95), (233, 172, 161), (152, 213, 190), (242, 205, 8), (89, 48, 31)]

from turtle import Turtle, Screen
import turtle as t
import random

tim = Turtle()
tim.speed('fastest')
t.colormode(255)

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

turn = 270
direction = 'left'

for i in range(100):
    if (i + 1) % 10 == 0:
        if direction == 'left':
            tim.left(90)
        else:
            tim.right(90)

    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)

    if (i + 1) % 10 == 0:
        if direction == 'left':
            tim.left(90)
            direction = 'right'
        else:
            tim.right(90)
            direction = 'left'



screen = Screen()
screen.exitonclick()