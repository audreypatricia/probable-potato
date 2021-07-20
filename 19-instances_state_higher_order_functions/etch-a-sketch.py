from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(20)


def move_backward():
    tim.backward(20)


# def clockwise():
#     current_direction = tim.heading()
#     if current_direction == 0:
#         current_direction = 360
#     tim.setheading(current_direction - 90)
#
#
# def counter_clockwise():
#     current_direction = -tim.heading()
#     current_direction -= 90
#     if current_direction == -360:
#         current_direction = 0
#     tim.setheading(abs(current_direction))

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()
