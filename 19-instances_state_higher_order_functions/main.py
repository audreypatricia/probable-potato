from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards) # event listener
screen.exitonclick()


# functions as inputs -  you can put functions as input such as move_forwards in the .onkey() method
# we do not use the parentheses () because it means that the function will run then and there
# these are higher order functions - a function that can work with other functions e.g. the onkey()
