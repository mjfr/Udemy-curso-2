from turtle import Turtle
from random import choice


class Target(Turtle):
    def __init__(self, xpos, ypos):
        super(Target, self).__init__()
        self.colors = ["red", "yellow", "white", "blue", "chartreuse", "magenta", "dark violet", "indigo", "orange"]
        self.penup()
        self.shape("square")
        self.color(choice(self.colors))
        self.goto(xpos, ypos)
        self.shapesize(stretch_len=5)
