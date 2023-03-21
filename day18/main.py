from turtle import Turtle, Screen, fd
import random
timmy = Turtle()
timmy.shape("turtle")
timmy.penup()
list = ["red", "blue", "silver", "medium slate blue"]

for _ in range(4):
    color = random.choice(list)
    timmy.color("black", color)
    timmy.begin_fill()
    for _ in range(4):
        timmy.forward(80)
        timmy.right(90)
    timmy.forward(100)
    timmy.end_fill()

my_screen = Screen()
my_screen.exitonclick()