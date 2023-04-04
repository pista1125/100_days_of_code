from turtle import Turtle

class Player:

    def __init__(self):
        self.player = []
        self.position_y = [40, 20, 0, -20, -40]
        self.position_x = -330

    def create(self):
        for item in range(5):
            timmy = Turtle()
            timmy.penup()
            timmy.goto(self.position_x, self.position_y[item])
            timmy.shape("square")
            self.player.append(timmy)