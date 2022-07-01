from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super(Paddle, self).__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.speed(0)
        self.setheading(180)
        self.goto(position)
        self.shapesize(stretch_len=5)

    def move_left(self):
        self.forward(20)

    def move_right(self):
        self.backward(20)

    def boundary_stopper(self, x_cor, min_max_x):
        if x_cor >= min_max_x:
            self.goto(min_max_x, self.ycor())
        if x_cor <= -min_max_x:
            self.goto(-min_max_x, self.ycor())
