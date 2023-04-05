from turtle import Turtle

class Player:

    def __init__(self):
        self.player_1_timmy = []
        self.player_2_timmy = []
        self.position_player_y = [40, 20, 0, -20, -40]
        self.position_1_player_x = -430
        self.position_2_player_x = 430
        self.setheading_1 = [60, 30, 0, 330, 300]
        self.setheading_2 = [120, 150, 180, 210, 240]

    def create_1player(self):
        for item in range(5):
            timmy = Turtle()
            timmy.setheading(90)
            timmy.penup()
            timmy.color("white")
            timmy.goto(self.position_1_player_x, self.position_player_y[item])
            timmy.shape("square")
            self.player_1_timmy.append(timmy)

    def create_2player(self):
        for item in range(5):
            timmy = Turtle()
            timmy.setheading(90)
            timmy.penup()
            timmy.color("white")
            timmy.goto(self.position_2_player_x, self.position_player_y[item])
            timmy.shape("square")
            self.player_2_timmy.append(timmy)

    def move_UP_1player(self):
        if self.player_1_timmy[0].ycor() < 230:
            for timmy in self.player_1_timmy:
                timmy.forward(20)

    def move_Down_1player(self):
        if self.player_1_timmy[4].ycor() > -230:
            for timmy in self.player_1_timmy:
                timmy.backward(20)

    def move_UP_2player(self):
        if self.player_2_timmy[0].ycor() < 230:
            for timmy in self.player_2_timmy:
                timmy.forward(20)

    def move_Down_2player(self):
        if self.player_2_timmy[4].ycor() > -230:
            for timmy in self.player_2_timmy:
                timmy.backward(20)

