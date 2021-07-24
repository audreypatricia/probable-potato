from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle('square')
        new_car.penup()
        new_car.shapesize(1, 2)
        new_car.color(random.choice(COLORS))
        new_car.goto(300, random.randint(-250, 250))
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_distance)

    def increase_car_speed(self):
        self.move_distance += MOVE_INCREMENT