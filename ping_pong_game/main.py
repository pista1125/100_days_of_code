from turtle import Screen
from player import Player
from ball import Ball


my_screen = Screen()
my_screen.setup(width=900, height=500)
my_screen.bgcolor("black")
my_screen.tracer(0)


player_1 = Player()
player_1.create_1player()

player_2 = Player()
player_2.create_2player()

ball = Ball()
my_screen.update()



my_screen.exitonclick()


