from turtle import Turtle, Screen
import random

my_sreen = Screen()
guess = my_sreen.textinput(title="Guess the winner", prompt="Who will win?")

color = ["red", "blue", "green", "yellow", "orange"]
y_position = [-200, -100, 0, 100, 200]
all_turtle = []

for timmy_index in range(0, 5):
    timmy = Turtle(shape="turtle")
    timmy.color(color[timmy_index])
    timmy.penup()
    timmy.goto(x=-200, y=y_position[timmy_index])
    all_turtle.append(timmy)

game_on = True
while game_on:
    for turtle in all_turtle:
        if turtle.xcor() > 290:
            game_on = False
            winning = turtle.pencolor()
            if winning == guess:
                print(f"You have won! The {winning} turtle is the winner!")
            else:
                print(f"You have lost! The {winning} turtle is the winner!")
        rand_distance = random.randint(-2, 10)
        turtle.forward(rand_distance)

my_sreen.exitonclick()