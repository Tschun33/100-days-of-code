from turtle import Turtle
import pandas as pd

pd.read_csv("50_states.csv")


class State(Turtle):
    def __init__(self, name, x, y):
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.penup()

    def right_guess(self):
        self.goto(self.x, self.y)
