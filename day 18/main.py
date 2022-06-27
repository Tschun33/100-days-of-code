from turtle import Turtle, Screen, color, begin_fill, forward, left, end_fill, done, pos
import random

stef_turtle = Turtle()
stef_turtle.pensize(1)
stef_turtle.speed(10)

screen = Screen()
colors = ["red", "yellow", "blue", "orange", "black", "green"]
i = 0
screen.colormode(255)


def random_color():
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    rand_color = (a, b, c)
    return rand_color


for x in range(21):
    angle = (360 / 20) * x
    stef_turtle.setheading(angle)
    stef_turtle.circle(50)

done()
