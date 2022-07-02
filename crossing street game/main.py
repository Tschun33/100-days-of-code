import time
from turtle import Turtle, Screen
from player import Player
from car import Car
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=400)
screen.tracer(0)
scoreboard = Scoreboard()
cars = []


player = Player()
for x in range(0, 40):
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
        if car.xcor() < -290:
            car.reset_car()
        if player.ycor() > 180:
            player.reset()
            for car in cars:
                car.level_up()
                car.reset_car()

    for car in cars:
        if car.distance(player) < 10:
            print("collision")
            scoreboard.game_over()
            game_playing = False






screen.exitonclick()