import time
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()


    def score_up(self):
        self.score += 1

    def game_over(self):
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def next_stage(self):
        self.write("Next stage in 4 seconds", align=ALIGNMENT, font=FONT)

