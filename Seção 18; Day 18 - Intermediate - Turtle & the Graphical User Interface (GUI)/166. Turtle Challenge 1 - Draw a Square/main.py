from turtle import Turtle, Screen

just_another_regular_turtle = Turtle()
just_another_regular_turtle.shape("turtle")
just_another_regular_turtle.color("lime green")
for _ in range(4):
    just_another_regular_turtle.forward(100)
    just_another_regular_turtle.right(90)

screen = Screen()
screen.exitonclick()
