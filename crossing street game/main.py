import time
from turtle import Turtle, Screen
from player import Player
from car import Car


screen = Screen()
screen.setup(width=800, height=400)
screen.tracer(0)

cars = []


player = Player()
for x in range(0, 50):
    new_car = Car()
    cars.append(new_car)


screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")


game_playing = True

while game_playing:
    time.sleep(0.1)
    screen.update()
    for car in cars:
        car.move()
        if car.xcor() < -390:
            car.reset_car()




screen.exitonclick()