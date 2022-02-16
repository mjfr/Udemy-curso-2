from turtle import Turtle

FONT = ("Courier", 24, "normal")
STANDARD_POSITION = (-290, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.stage = 0
        self.goto(STANDARD_POSITION)
        self.write(arg=f"Stage: {self.stage}", align="left", font=FONT)

    def refresh_scoreboard(self):
        self.clear()
        self.goto(STANDARD_POSITION)
        self.write(arg=f"Stage: {self.stage}", align="left", font=FONT)

    def level_up(self):
        self.stage += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
