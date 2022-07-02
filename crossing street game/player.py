from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.start_x = 0
        self.start_y = -180
        self.penup()
        self.setheading(90)
        self.goto(self.start_x, self.start_y)
        self.level = 1

    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(self.start_x, new_y)

    def move_down(self):
        new_y = self.ycor() - 10
        self.goto(self.start_x, new_y)

    def reset(self):
        self.goto(self.start_x, self.start_y)


