from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.goto(0, 275)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("Segoe ui", 14, "italic bold"))

    def add_score(self):
        self.score += 1
