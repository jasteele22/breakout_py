from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self,):
        super().__init__()
        self.score = 0
        self.color("white")
        self.ht()
        self.penup()
        self.setposition(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score}", align="center", font=("Courier", 50, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        if self.score == 152:
            game_is_on = False
            return game_is_on
        else:
            game_is_on = True
            return game_is_on

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align='center', font=('Courier', 48, "bold"))
