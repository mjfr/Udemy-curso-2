from turtle import Turtle, Screen
import random

tobias = Turtle("turtle")
tobias.speed(0)

while True:
    for _ in range(12):
        tobias.forward(30)
        tobias.right(15)
    if abs(tobias.pos()) < 1:
        break

screen = Screen()
screen.exitonclick()