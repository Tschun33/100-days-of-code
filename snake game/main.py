import time
from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Tschuns Snake game")

screen.tracer(0)

turtles = []
x_start = 0
y_start = 0
x_shift = 0

for turtle_index in range(0,3):
    stef = Turtle()
    stef.shape("square")
    stef.penup()
    stef.color("white")
    stef.setx(x_shift)
    x_shift -= 20
    turtles.append(stef)

screen.update()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(turtles)-1, 0, -1):
        new_x = turtles[seg_num-1].xcor()
        new_y = turtles[seg_num-1].ycor()
        turtles[seg_num].goto(new_x, new_y)
    turtles[0].forward(20)







screen.exitonclick()