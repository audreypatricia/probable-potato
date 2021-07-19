from turtle import Turtle, Screen
# you can alias imports e.g.
import turtle as t
# you can create a turtle using t.Turtle()

tim = Turtle()
tim.shape("turtle")
tim.color('red')

# getting tim to draw a square
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# getting tim to draw a dashed line
# for i in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

# getting tim to draw all sorts of shapes
# angles = []
# sides = [3, 4, 5, 6, 7, 8, 9, 10]
# colors = ['cornflowerBlue', 'darkOrange', 'deepPink', 'firebrick', 'goldenrod', 'indianRed', 'lightCoral', 'lawnGreen']
#
# for i in range(3, 11):
#     angles.append(360 / i)
#
#
# for index, angle in enumerate(angles):
#     for _ in range(sides[index]):
#         tim.color(colors[index])
#         tim.forward(100)
#         tim.right(angle)


# better solution to get tim to draw all sorts of shapes

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)

# use random.choice() to take a random color from a list of colors

# Getting tim to do a random walk
import random

# turns = [0, 90, 180, 270]
colors = ['cornflowerBlue', 'darkOrange', 'deepPink', 'firebrick', 'goldenrod', 'indianRed', 'lightCoral', 'lawnGreen']
# tim.speed('fast')

# using tuples for random colors:

# t.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color_tuple = (r, g, b)
#     return color_tuple
#
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.pensize(10)
#     tim.forward(30)
#     tim.setheading(random.choice(turns))


# Python tuples - are a data type in python (1, 3, 8) like a list but with paranthesis seperated by commas
my_tuple = (1, 3, 8)
my_tuple[2] # this will be '8'

# difference between tuple and lists? - you cannot change the value of a tuple (it is immutable)
# if you suddenly realise you want to change a tuple cast it into a list
list(my_tuple)

# Getting tim to draw a spirograph
tim.speed('fastest')


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random.choice(colors))
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()