from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.penup()
        self.possible_location = []
        self.create_object()


    def create_object(self):
        for x in range(-280, 280):
            if x % 20 == 0:
                self.possible_location.append(x)
        self.goto(random.choice(self.possible_location), random.choice(self.possible_location))


