from turtle import Turtle, Screen
import time
from snake import Snake

my_screen = Screen()

my_screen.setup(width=550, height=550)
my_screen.bgcolor("black")
my_screen.title("My snake game")
my_screen.tracer(0)

snake = Snake()

my_screen.listen()
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")


game_on = True
while game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()











my_screen.exitonclick()