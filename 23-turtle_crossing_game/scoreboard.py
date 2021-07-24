from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-250, 250)

    def increase_level(self):
        self.level += 1

    def write_board(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align="center", font=FONT)

