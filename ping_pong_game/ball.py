from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()



    def move(self):
        self.penup()
        self.shape("circle")
        self.setheading(90)
        self.forward(20)