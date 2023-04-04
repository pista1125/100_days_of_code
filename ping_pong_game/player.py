from turtle import Turtle

class Player:

    def __init__(self):
        self.player_1_timmy = []
        self.player_2_timmy = []
        self.position_player_y = [40, 20, 0, -20, -40]
        self.position_1_player_x = -430
        self.position_2_player_x = 430

    def create_1player(self):
        for item in range(5):
            timmy = Turtle()
            timmy.penup()
            timmy.color("white")
            timmy.goto(self.position_1_player_x, self.position_player_y[item])
            timmy.shape("square")
            self.player_1_timmy.append(timmy)

    def create_2player(self):
        for item in range(5):
            timmy = Turtle()
            timmy.penup()
            timmy.color("white")
            timmy.goto(self.position_2_player_x, self.position_player_y[item])
            timmy.shape("square")
            self.player_2_timmy.append(timmy)