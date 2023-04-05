from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score_1 = 0
        self.score_2 = 0


    def player_1_score(self):
        self.goto(-100, 160)
        self.write(arg=f"{self.score_1}", move=False, align="center", font=("pixel", 60, "normal"))

    def player_2_score(self):
        self.goto(100, 160)
        self.write(arg=f"{self.score_2}", move=False, align="center", font=("pixel", 60, "normal"))

    def score_add_1(self):
        self.score_1 += 1
        self.clear()
        self.write(arg=f"{self.score_1}", move=False, align="center", font=("pixel", 60, "normal"))

    def score_add_2(self):
        self.score_2 += 1
        self.clear()
        self.write(arg=f"{self.score_2}", move=False, align="center", font=("pixel", 60, "normal"))