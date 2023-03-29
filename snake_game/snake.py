from turtle import Turtle, Screen
from food import Food
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.starting_position = [(0, 0), (-20, 0), (-40, 0)]
        self.timmy_snake = []
        self.timmy_head = None
        self.color = "white"
        self.pause_button = 1
        self.robot_button = 0
        self.c = -1

    def create_snake(self):
        for new_segment in self.starting_position:
            self.add_segment(new_segment)
        self.timmy_head = self.timmy_snake[0]

    def add_segment(self, position):
        timmy = Turtle(shape="square")
        timmy.color(self.color)
        timmy.penup()
        timmy.goto(position)
        self.timmy_snake.append(timmy)

    def move(self):
        for item in range(len(self.timmy_snake) - 1, 0, -1):
            new_x = self.timmy_snake[item - 1].xcor()
            new_y = self.timmy_snake[item - 1].ycor()
            self.timmy_snake[item].goto(new_x, new_y)
        self.timmy_snake[0].forward(MOVE_DISTANCE)

    def plus_snake(self):
        self.add_segment(self.timmy_snake[-1].position())

    def wall_bounce_x(self):
        x = self.timmy_head.xcor()
        y = self.timmy_head.ycor()
        self.timmy_head.goto(-x, y)

    def wall_bounce_y(self):
        x = self.timmy_head.xcor()
        y = self.timmy_head.ycor()
        self.timmy_head.goto(x, -y)

    def position(self):
        self.starting_position = [(0, -40), (-20, -40), (-40, -40)]
        self.color = "green"

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

    def remove_tails(self):
        for item in self.timmy_snake[3:]:
            item.hideturtle()
        self.timmy_snake = self.timmy_snake[:3]

    def pause(self):
        self.pause_button += 1

    def robot_pilot(self):
        self.robot_button += 1
        self.c += 1

    def robot_pilot_move(self):
        self.remove_tails()
        self.timmy_head.goto(-260, -260)
        self.timmy_head.setheading(90)
        self.c += 1

