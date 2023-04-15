from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

my_screen = Screen()

my_screen.title("Pong")
my_screen.bgcolor("black")
my_screen.setup(width=800, height=600)
my_screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

my_screen.listen()

my_screen.onkey(r_paddle.go_up, "Up")
my_screen.onkey(r_paddle.go_down, "Down")
my_screen.onkey(l_paddle.go_up, "w")
my_screen.onkey(l_paddle.go_down, "s")

game_on = True

while game_on:
    my_screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()


    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()


my_screen.exitonclick()
