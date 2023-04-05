from turtle import Turtle

class Field:

    def __init__(self):
        self.position_y = []
        self.position_x = 0

    def create_field(self):
        for item in range(-250, 250, 20):
            self.position_y.append(item)

        for x in range(25):
            field = Turtle()
            field.shape("square")
            field.color("white")
            field.penup()
            field.shapesize(0.5, 0.25)
            field.goto(self.position_x, int(self.position_y[x]))