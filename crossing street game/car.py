import random
from turtle import Turtle

colors = ["red", "blue", "green", "yellow", "orange", "purple", "black", "brown"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.start_x = random.randint(390, 1190)
        self.start_y = random.randint(-160, 160)
        self.shapesize(stretch_wid=0.5, stretch_len=1)
        self.color(random.choice(colors))
        self.shape("square")
        self.penup()
        self.setheading(180)
        self.goto(self.start_x, self.start_y)
        self.car_level = 1

    def move(self):
        new_x = self.xcor() - (10 * self.car_level)
        self.goto(new_x, self.ycor())

    def reset_car(self):
        self.goto(self.start_x, self.ycor())

    def level_up(self):
        self.car_level += 0.2

