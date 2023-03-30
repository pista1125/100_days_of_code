from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update_score()

    def update_score(self):
        self.write(f"Your score is: {self.score}", False, "center", ("Arial", 12, "normal"))

    def score_add(self):
        self.score += 1
        self.clear()
        self.update_score()

    def score_extra_add(self):
        self.score += 3
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game over", False, "center", ("Arial", 12, "normal"))