from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.screensize(800, 600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

ball = Ball()
scoreboard = Scoreboard()
game_is_on = True


def end_game():
    global game_is_on
    game_is_on = False
    writing = Turtle()
    writing.pencolor('white')
    writing.write("Game Over", align="center", font=("Courier", 80, "normal"))


screen.listen()
screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')
screen.onkey(end_game, 'a')


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # check collision to top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # check collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # check if the ball was not caught by the paddle
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()



screen.exitonclick()
