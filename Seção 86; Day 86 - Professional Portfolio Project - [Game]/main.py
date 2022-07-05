# TODO 1 - Using Python Turtle, build a clone of the 80s game: Breakout
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
from targets import Target
from turtle import Screen
from time import sleep


def run():
    screen = Screen()
    screen.title("Breakout")
    screen.setup(width=700, height=800)
    screen.bgcolor("black")
    screen.listen()
    screen.tracer(0)
    scoreboard = Scoreboard()
    player_paddle = Paddle((0, -200))
    ball = Ball()
    x_pos_list = [270 - 110 * x for x in range(6)]
    y_pos_list = [380 - 25 * y for y in range(5)]
    target_list = [Target(x, y) for x in x_pos_list for y in y_pos_list]

    screen.onkeypress(key="Left", fun=player_paddle.move_left)
    screen.onkeypress(key="Right", fun=player_paddle.move_right)
    while True:
        screen.update()
        player_paddle.boundary_stopper(x_cor=player_paddle.xcor(), min_max_x=300)
        sleep(ball.move_speed)
        ball.move()
        ball.boundary_bounce_x(x_cor=ball.xcor(), min_max_x=330)
        ball.boundary_bounce_y(y_cor=ball.ycor(), max_y=390)
        out_of_boundary = ball.out_of_boundary_y(y_cor=ball.ycor(), min_y=-390, x_cor=player_paddle.xcor())
        ball.detect_paddle_collision(player_paddle)
        for target in target_list:
            ball.detect_target_collision(target, target_list, scoreboard)
        if out_of_boundary:
            scoreboard.lose_life()
        if scoreboard.win_game(target_list):
            break
        if scoreboard.game_over():
            break

    screen.exitonclick()


run()
