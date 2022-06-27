from turtle import Turtle

x_shift = 0
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake(x_shift)
        self.head = self.segments[0]

    def create_snake(self, x_shift):
        for turtle_index in range(0, 3):
            stef = Turtle()
            stef.shape("square")
            stef.penup()
            stef.color("white")
            stef.setx(x_shift)
            x_shift -= 20
            self.segments.append(stef)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self):
        last_segment = self.segments[(len(self.segments)-1)]
        last_x = last_segment.xcor()
        last_y = last_segment.ycor()
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(last_x, last_y)
        self.segments.append(new_segment)


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
