from turtle import Turtle, Screen

tortuga = Turtle("turtle")
tortuga.color("purple")

for _ in range(20):
    tortuga.pendown()
    tortuga.forward(5)
    tortuga.penup()
    tortuga.forward(5)


screen = Screen()
screen.exitonclick()
