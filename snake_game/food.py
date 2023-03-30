from turtle import Turtle
import random
from game_input import Game_input

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.possible_location = []
        self.x_pos = self.xcor()
        self.y_pos = self.ycor()
        self.food_number = 1

    def create_object(self):
        for x in range(-260, 260):
            if x % 20 == 0:
                self.possible_location.append(x)
        if self.food_number % 5 != 0:
            self.color("blue")
            self.shapesize(1, 1)
            self.goto(random.choice(self.possible_location), random.choice(self.possible_location))
            self.x_pos = self.xcor()
            self.y_pos = self.ycor()
            self.food_number += 1
        elif self.food_number % 5 == 0:
            self.color("red")
            self.shapesize(stretch_wid=1.5, stretch_len=1.5)
            self.goto(random.choice(self.possible_location), random.choice(self.possible_location))
            self.x_pos = self.xcor()
            self.y_pos = self.ycor()
            self.food_number += 1
    # def change_food_color(self):
    #     color = Game_input()
    #     self.color_food = color.color_choice


