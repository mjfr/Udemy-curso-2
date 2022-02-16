from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

screen = Screen()
screen.title("PyPong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.onkeypress(key="Up", fun=right_paddle.up)
screen.onkeypress(key="Down", fun=right_paddle.down)
screen.onkeypress(key="w", fun=left_paddle.up)
screen.onkeypress(key="s", fun=left_paddle.down)

is_game_on = True
while is_game_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # print("Collision with wall")
        ball.bounce_y()

    # Detecting collision with paddles
    if ball.distance(right_paddle) < 65 and ball.xcor() > 320 or ball.distance(left_paddle) < 65 and ball.xcor() < -320:
        # print("Collision with right paddle")
        ball.bounce_x()

    # Detecting misses from paddles
    if ball.xcor() > 380:
        # print("Left paddle's score")
        ball.reset_position()
        scoreboard.left_point()
    elif ball.xcor() < -380:
        # print("Right paddle's score")
        ball.reset_position()
        scoreboard.right_point()

    print(ball.move_speed)

screen.exitonclick()
