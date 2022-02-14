from turtle import Turtle, Screen

billy = Turtle()
screen = Screen()


def move_forwards():
    billy.forward(10)


screen.listen()

# Higher Order Functions são funções que trabalham com outras funções. .onkey() é um exemplo de Higher Order Function
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()