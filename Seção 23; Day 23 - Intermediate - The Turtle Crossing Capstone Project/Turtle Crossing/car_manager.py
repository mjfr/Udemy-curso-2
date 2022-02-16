from turtle import Turtle
from random import choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
MOVE_DIRECTION = 180


class CarManager(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(choice(COLORS))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.setposition(position)
        self.car_speed = STARTING_MOVE_DISTANCE

    def move(self):
        self.backward(self.car_speed)

    def speed_increase(self, stage):
        self.car_speed += MOVE_INCREMENT * stage

    def car_clear(self):
        self.reset()
        self.penup()
        self.goto(400, 400)
        self.hideturtle()
