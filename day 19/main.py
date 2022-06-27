import turtle
from random import random, randint
from turtle import Turtle, Screen, done
is_playing = False
colors = ["green", "blue", "red", "yellow", "orange", "purple"]
screen = Screen()
screen.setup(width= 500, height= 400)
user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a color: ")

turtles = []
winner = ""
pos_y = 150
pos_x = -200
y_down = 0
for turtle_index in range(0,6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    y_start = float(pos_y - y_down)
    turtle.goto(x=pos_x, y=y_start)
    y_down += 25
    turtles.append(turtle)

if user_bet:
    is_playing = True

while is_playing:
    for turtle in turtles:
        turtle.forward(randint(0, 4))
    if turtle.xcor() >= 200:
        winner = turtle.pencolor()
        is_playing = False

print(f"winner is {winner}")


screen.exitonclick()