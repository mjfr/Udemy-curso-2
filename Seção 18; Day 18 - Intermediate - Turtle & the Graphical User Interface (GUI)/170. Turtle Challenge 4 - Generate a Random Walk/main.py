from turtle import Turtle, Screen
import random

leo = Turtle("turtle")
leo_colors = ["dark slate blue", "red", "lime green", "black", "orange", "pink", "yellow", "purple"]
leo.speed(0)
leo.width(10)

limit = 200
leo_direction = [0, 90, 180, 270]
while limit != 0:
    for _ in range(2):
        leo.setheading(random.choice(leo_direction))
        leo.forward(50)
        leo.color(random.choice(leo_colors))
    limit -= 1


screen = Screen()
screen.exitonclick()
