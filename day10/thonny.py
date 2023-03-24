from turtle import Turtle, Screen
import random
timmy = Turtle()
timmy.shape("turtle")

list = ["red", "blue", "silver", "medium slate blue"]

for x in range(3):
    color = random.choice(list)
    timmy.color(color)
    a = int(360 / (x+3))
    for y in range(a):
        timmy.right(a)
        timmy.forward(100)

my_screen = Screen()
my_screen.exitonclick()