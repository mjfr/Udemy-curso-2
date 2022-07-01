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
        self.move_speed = 1/1000*60
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
        paddle_center = (x_cor + randint(-50, 50), -150)
        if randint(1, 2) == 1:
            self.bounce_x()
        self.goto(paddle_center)

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

    # def detect_paddle_collision(self, paddle):
    #     if -100 < paddle.xcor() > 100 and self.ycor() < -179:
    #         print(paddle)
    #         self.bounce_y()

