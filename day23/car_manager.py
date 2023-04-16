from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.y_cor = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def starting_y(self):
        for x in range(-250, 250):
            if x % 20 == 0:
                self.y_cor.append(x)

    def create_cars(self):
        chance = random.randint(0, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            self.starting_y()
            new_car.goto(300, random.choice(self.y_cor))
            self.all_cars.append(new_car)

    def move_all_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT