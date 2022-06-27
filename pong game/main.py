from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()


game_on = True
screen.tracer(0)
l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
screen.tracer(1)

screen.onkey(r_paddle.paddle_up, "Up")
screen.onkey(r_paddle.paddle_down, "Down")
screen.onkey(l_paddle.paddle_up, "w")
screen.onkey(l_paddle.paddle_down, "s")

screen.exitonclick()