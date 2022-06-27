from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, start_x, start_y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.setheading(90)
        self.penup()
        self.goto(start_x, start_y)

    def paddle_up(self):
        new_y = self.ycor() + 20
        static_x = self.xcor()
        self.goto(static_x, new_y)

    def paddle_down(self):
        new_y = self.ycor() - 20
        static_x = self.xcor()
        self.goto(static_x, new_y)
