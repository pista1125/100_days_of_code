from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.penup()
        self.possible_location = []
        self.x_pos = self.xcor()
        self.y_pos = self.ycor()

    def create_object(self):
        for x in range(-260, 260):
            if x % 20 == 0:
                self.possible_location.append(x)
        self.goto(random.choice(self.possible_location), random.choice(self.possible_location))
        self.x_pos = self.xcor()
        self.y_pos = self.ycor()


