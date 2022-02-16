from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courrier", 16, "bold")


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
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", move=False, align=ALIGNMENT, font=FONT)
