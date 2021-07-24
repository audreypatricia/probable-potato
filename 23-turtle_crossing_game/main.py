import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

car_manager = CarManager()
screen.listen()
screen.onkey(player.move, 'Up')

counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.write_board()
    counter += 1
    if counter == 6:
        car_manager.create_car()
        counter = 0
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    # check if turtle has made it to the finish line
    if player.is_at_finish_line():
        player.reset_turtle()
        car_manager.increase_car_speed()
        scoreboard.increase_level()

screen.exitonclick()
