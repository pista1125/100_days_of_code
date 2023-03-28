#Snake game

from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score
from game_start import GameStart
from game_input import Game_input

my_screen = Screen()

my_screen.title("Snake game")
my_screen.bgcolor("black")
my_screen.setup(width=560, height=560)
my_screen.tracer(0)


game = Game_input()

game.player()
while game.player_number == 0:
    my_screen.onclick(game.choice_number, btn=1)
    my_screen.update()
game.all_timmy_clear()

game.speed_turtle()
while game.speed == 0:
    my_screen.onclick(game.choice_speed, btn=1)
    my_screen.update()
game.all_timmy_clear()

game.wall_turtle()
while game.bounce_wall == 0:
    my_screen.onclick(game.choice_bounce, btn=1)
    my_screen.update()
game.all_timmy_clear()


game_start = GameStart()

for x in range(3):
    game_start.Start()
    time.sleep(1)
    game_start.clear()

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

    if snake.timmy_head.xcor() > 280 or snake.timmy_head.xcor() < -280 or snake.timmy_head.ycor() > 280 or snake.timmy_head.ycor() < -280:
        score.game_over()
        game_on = False

    for timmy in snake.timmy_snake[1:]:
        if snake.timmy_head.distance(timmy) < 10:
            score.game_over()
            game_on = False



my_screen.mainloop()


#try

# from turtle import Turtle, Screen
#
# def go(x, y):
#     if x > 0:
#         timmy.goto(100, 0)
#     if x < 0:
#         timmy.goto(-100, 0)
#     print(x, y)
#
#
# timmy = Turtle()
# my_screen = Screen()
#
# a = my_screen.onclick(go, btn=1)
#
# print(a)
#
# my_screen.mainloop()





