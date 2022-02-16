from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
MOVE_DIRECTION = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(MOVE_DIRECTION)
        self.setpos(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def next_level(self):
        self.goto(STARTING_POSITION)
