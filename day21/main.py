#1. work with classes

# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#
#     def breathe(self):
#         print("Inhale, exhale")
#
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#
#     def breathe(self):
#         super().breathe()
#         print("doing this underwater")
#     def swim(self):
#         print("moving in water")
#
#
# nemo = Fish()
#
# nemo.swim()
# nemo.breathe()
# print(nemo.num_eyes)








#2. Snake game

from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score

my_screen = Screen()



my_screen.setup(width=560, height=560)
my_screen.bgcolor("black")
my_screen.title("My snake game")
my_screen.tracer(0)
#hello

# b = my_screen.textinput("level", "choice")
# if b == "hard":
#     a = 0.01
# if b == "normal":
#     a = 0.1
# if b == "easy":
#     a = 0.3

snake = Snake()
food = Food()
score = Score()

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
    if snake.timmy_head.distance(food) < 10:
        food.create_object()
        snake.plus_snake()
        score.score_add()




my_screen.exitonclick()