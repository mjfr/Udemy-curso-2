from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_instances = []
X_POS = -230
y_pos = -100
is_race_on = False

for color in COLORS:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=X_POS, y=y_pos)
    turtle_instances.append(new_turtle)
    y_pos += 33.3333334

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_instances:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
                is_race_on = False
            else:
                print(f"You've lost! The { winning_color} turtle is the winner!")
                is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

print(turtle_instances)

screen.exitonclick()
