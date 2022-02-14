from turtle import Turtle, Screen

# W --> Forwards
# S --> Backwards
# A --> Counter-Clockwise
# D --> Clockwise
# C --> Clear drawing

patrick = Turtle()
screen = Screen()


def move_forwards():
    patrick.forward(10)


def move_backwards():
    patrick.backward(10)


def counter_clockwise_turn():
    patrick.left(10)


def clockwise_turn():
    patrick.right(10)


def clear_screen():
    patrick.reset()


exit_condition = False


def keep_going():
    return True


while not exit_condition:
    screen.listen()
    screen.onkey(key="w", fun=move_forwards)
    screen.onkey(key="s", fun=move_backwards)
    screen.onkey(key="a", fun=counter_clockwise_turn)
    screen.onkey(key="d", fun=clockwise_turn)
    screen.onkey(key="c", fun=clear_screen)
    screen.onkey(key="e", fun=keep_going)
    exit_condition = keep_going()

screen.exitonclick()

