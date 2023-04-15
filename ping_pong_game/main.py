from turtle import Screen
from player import Player
from ball import Ball
from field import Field
from score import Score
import time

HEIGHT = 500
WIDTH = 900
my_screen = Screen()
my_screen.setup(width=WIDTH, height=HEIGHT)
my_screen.bgcolor("black")
my_screen.tracer(0)


player = Player()
player.create_1player()

player.create_2player()

ball = Ball()

field = Field()
field.create_field()

score_1 = Score()
score_1.player_1_score()

score_2 = Score()
score_2.player_2_score()

my_screen.update()


my_screen.listen()
my_screen.onkeypress(player.move_UP_1player, "Up")
my_screen.onkeypress(player.move_Down_1player, "Down")
my_screen.onkeypress(player.pause, "space")
my_screen.onkeypress(player.move_UP_2player, "w")
my_screen.onkeypress(player.move_Down_2player, "s")

game_on = True
while game_on:
    my_screen.update()
    time.sleep(0.005)
    if player.pause_button % 2 != 0:
        ball.move()

    #pause button
    if player.pause_button % 2 == 0:
        while player.pause_button % 2 == 0:
            time.sleep(1)
            my_screen.update()

    #collision with player
    for x in range(5):
        if player.player_1_timmy[x].distance(ball) < 20:
            ball.setheading(player.setheading_1[x])
        if player.player_2_timmy[x].distance(ball) < 20:
            ball.setheading(player.setheading_2[x])

    #collision with wall

    if abs(ball.ycor()) > int(HEIGHT / 2):
        head = ball.heading()
        ball.setheading(360 - head)

    if ball.xcor() > int(WIDTH / 2):
        score_1.score_add_1()
        time.sleep(1)
        ball.start_2()
        player.pause()
        while player.pause_button % 2 == 0:
            #time.sleep(0.1)
            my_screen.update()

    elif ball.xcor() < - int(WIDTH / 2):
        score_2.score_add_2()
        time.sleep(1)
        ball.start_1()
        player.pause()
        while player.pause_button % 2 == 0:
            #time.sleep(0.1)
            my_screen.update()

my_screen.exitonclick()


