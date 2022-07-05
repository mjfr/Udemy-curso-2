from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.player_score = 0
        self.lives = 5
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, -300)
        self.write(f"Score: {self.player_score}\tLives: {self.lives}", align="center", font=("Consolas", 30, "bold"))

    def add_score(self):
        self.player_score += 1
        self.update_score()

    def lose_life(self):
        self.lives -= 1
        self.update_score()

    def game_over(self):
        if self.lives == 0:
            self.color("red")
            self.goto(0, 0)
            self.write("  GAME OVER!\nClick to Exit", align="center", font=("Consolas", 60, "bold"))
            return True
        return False

    def win_game(self, target_list: list):
        if len(target_list) == 0:
            self.color("chartreuse")
            self.goto(0, 0)
            self.write("  YOU WIN!\nClick to Exit", align="center", font=("Consolas", 60, "bold"))
            return True
        return False

