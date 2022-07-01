# TODO 1 - Using Python Turtle, build a clone of the 80s game: Breakout
from paddle import Paddle
from ball import Ball
from turtle import Screen
from time import sleep
# Classe pra bola??
# Classe pros bloquinhos??
# Classe pro placar??

screen = Screen()
screen.title("Breakout")
screen.setup(width=700, height=800)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

player_paddle = Paddle((0, -200))
ball = Ball()

screen.onkeypress(key="Left", fun=player_paddle.move_left)
screen.onkeypress(key="Right", fun=player_paddle.move_right)

while True:
    screen.update()
    player_paddle.boundary_stopper(x_cor=player_paddle.xcor(), min_max_x=300)
    sleep(ball.move_speed)
    ball.move()
    ball.boundary_bounce_x(x_cor=ball.xcor(), min_max_x=330)
    ball.boundary_bounce_y(y_cor=ball.ycor(), max_y=390)
    ball.out_of_boundary_y(y_cor=ball.ycor(), min_y=-390, x_cor=player_paddle.xcor())
    ball.detect_paddle_collision(player_paddle)

screen.exitonclick()
