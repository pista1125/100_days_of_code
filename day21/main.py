from turtle import Turtle, Screen
import time
from snake import Snake
from object import Object
my_screen = Screen()



my_screen.setup(width=560, height=560)
my_screen.bgcolor("black")
my_screen.title("My snake game")
my_screen.tracer(0)

# b = my_screen.textinput("level", "choice")
# if b == "hard":
#     a = 0.01
# if b == "normal":
#     a = 0.1
# if b == "easy":
#     a = 0.3

snake = Snake()
#helo ebllo

my_screen.listen()
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")

object = Object()

game_on = True
while game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()