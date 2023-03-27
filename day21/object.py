from turtle import Turtle
import random


class Object:
    def __init__(self):
        self.possible_location = []
        self.create_object()

    def create_object(self):
        for x in range(-280, 280):
            if x % 20 == 0:
                self.possible_location.append(x)
        object = Turtle("square")
        object.penup()
        object.color("white")
        object.goto(random.choice(self.possible_location), random.choice(self.possible_location))
