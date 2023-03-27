from turtle import Turtle, Screen
import time

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.timmy_snake = []
        self.create_snake()

    def create_snake(self):
        for new_segment in STARTING_POSITION:
            timmy = Turtle(shape="square")
            timmy.color("white")
            timmy.penup()
            timmy.goto(new_segment)
            self.timmy_snake.append(timmy)

    def move(self):
        for item in range(len(self.timmy_snake) - 1, 0, -1):
            new_x = self.timmy_snake[item - 1].xcor()
            new_y = self.timmy_snake[item - 1].ycor()
            self.timmy_snake[item].goto(new_x, new_y)
        self.timmy_snake[0].forward(MOVE_DISTANCE)

    def left(self):
        if self.timmy_snake[0].heading() == UP or self.timmy_snake[0].heading() == DOWN:
            self.timmy_snake[0].setheading(LEFT)

    def right(self):
        if self.timmy_snake[0].heading() == UP or self.timmy_snake[0].heading() == DOWN:
            self.timmy_snake[0].setheading(RIGHT)

    def up(self):
        if self.timmy_snake[0].heading() == RIGHT or self.timmy_snake[0].heading() == LEFT:
            self.timmy_snake[0].setheading(UP)

    def down(self):
        if self.timmy_snake[0].heading() == RIGHT or self.timmy_snake[0].heading() == LEFT:
            self.timmy_snake[0].setheading(DOWN)
