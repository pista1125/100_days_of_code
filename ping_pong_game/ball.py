from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")

    def move(self):
        self.forward(10)

    def start_1(self):
        self.setheading(180)
        self.goto(0, 0)

    def start_2(self):
        self.setheading(0)
        self.goto(0, 0)