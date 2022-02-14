from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Humble Snake Game")

snake_turtle = []
initial_x = 0

for _ in range(0, 3):
    new_square = Turtle(shape="square")
    new_square.penup()
    new_square.color("white")
    new_square.backward(initial_x)
    snake_turtle.append(new_square)
    initial_x += 20

# for turtle in snake_turtle:


print(snake_turtle)


screen.exitonclick()
