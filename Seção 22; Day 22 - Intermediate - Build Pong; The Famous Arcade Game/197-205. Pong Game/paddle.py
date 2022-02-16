from turtle import Turtle
MOVEMENT_SPACING = 20
VERTICAL = 90


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(VERTICAL)
        self.color("white")
        self.goto(position)
        self.shapesize(stretch_len=5)

    def up(self):
        self.forward(MOVEMENT_SPACING)

    def down(self):
        self.backward(MOVEMENT_SPACING)
