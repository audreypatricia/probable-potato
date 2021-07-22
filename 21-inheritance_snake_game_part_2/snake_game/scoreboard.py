from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 260)
        self.pencolor("white")
        self.hideturtle()
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Scoreboard: {self.score} ", move=False, align=ALIGNMENT, font=FONT)
        self.speed("fastest")

    def add_point(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER ", move=False, align=ALIGNMENT, font=FONT)
