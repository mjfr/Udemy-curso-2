from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 36/1000
        self.reset_position(0)

    def move(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x_pos, y_pos)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self, x_cor):
        self.bounce_y()
        paddle_center_offset = (x_cor + randint(-50, 50), -179)
        if randint(1, 2) == 1:
            self.bounce_x()
        self.goto(paddle_center_offset)

    def boundary_bounce_x(self, x_cor, min_max_x):
        if x_cor >= min_max_x:
            self.bounce_x()
        if x_cor <= -min_max_x:
            self.bounce_x()

    def boundary_bounce_y(self, y_cor, max_y):
        if y_cor >= max_y:
            self.bounce_y()

    def out_of_boundary_y(self, y_cor, min_y, x_cor):
        if y_cor <= min_y:
            self.reset_position(x_cor)
            self.bounce_y()
            return True
        return False

    def detect_paddle_collision(self, paddle):
        if self.pos()[0] - 60 <= paddle.pos()[0] <= self.pos()[0] + 60 and\
                self.pos()[1] - 20 <= paddle.pos()[1] <= self.pos()[1] + 20:
            self.bounce_y()

    def detect_target_collision(self, target, target_list, scoreboard):
        if self.xcor() - 54 <= target.xcor() <= self.xcor() + 54 and \
                self.ycor() - 11 <= target.ycor() <= self.ycor() + 11:
            target.hideturtle()
            target.goto(700, 800)
            target_list.remove(target)
            self.bounce_y()
            scoreboard.add_score()

