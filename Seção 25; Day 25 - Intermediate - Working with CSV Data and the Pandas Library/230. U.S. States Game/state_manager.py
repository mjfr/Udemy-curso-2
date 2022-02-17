from turtle import Turtle
FONT_STATES = ("Courier", 8, "italic")
FONT_VICTORY = ("Courier", 32, "bold italic")


class State(Turtle):
    def __init__(self, position, state_name):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.write(state_name, align="center", font=FONT_STATES)

    def win(self):
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("You guessed all states\nYou Win!", align="center", font=FONT_VICTORY)

