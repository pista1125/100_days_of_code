#Snake game
def robot(player):
    if player.c % 3 == 0:
        player.robot_pilot_move()
    for x in range(26):
        if player.timmy_head.distance(food) < 10:
            food.create_object()
            player.plus_snake()
            score.score_add()
        player.move()
        my_screen.update()
        time.sleep(0.02)
    player.timmy_head.right(90)
    if player.timmy_head.distance(food) < 10:
        food.create_object()
        player.plus_snake()
        score.score_add()
    player.move()
    my_screen.update()
    player.timmy_head.right(90)
    for x in range(26):
        if player.timmy_head.distance(food) < 10:
            food.create_object()
            player.plus_snake()
            score.score_add()
        player.move()
        my_screen.update()
        time.sleep(0.02)
    player.timmy_head.left(90)
    if player.timmy_head.distance(food) < 10:
        food.create_object()
        player.plus_snake()
        score.score_add()
    player.move()
    my_screen.update()
    player.timmy_head.left(90)

def robot_2():
    food_x = food.x_pos
    food_y = food.y_pos
    snake_x = snake.timmy_head.xcor()
    snake_y = snake.timmy_head.ycor()
    snake_head = snake.timmy_head.heading()
    if food_x >= snake_x and food_y >= snake_y:
        if snake_head == 180:
            snake.timmy_head.setheading(90)
            my_screen.update()
            snake.timmy_head.setheading(0)
            my_screen.update()
        elif snake_head != 180:
            snake.timmy_head.setheading(0)
            my_screen.update()
        distance_x = round((food_x - snake_x) / 20)
        for step in range(distance_x):
            snake.move()
            my_screen.update()
            time.sleep(0.02)
        snake.timmy_head.setheading(90)
        distance_y = round((food_y - snake_y) / 20)
        for step in range(distance_y):
            snake.move()
            if snake.timmy_head.distance(food) < 10:
                food.create_object()
                snake.plus_snake()
                score.score_add()
            my_screen.update()
            time.sleep(0.02)
    elif food_x >= snake_x and food_y <= snake_y:
        if snake_head == 180:
            snake.timmy_head.setheading(90)
            my_screen.update()
            snake.timmy_head.setheading(0)
            my_screen.update()
        elif snake_head != 180:
            snake.timmy_head.setheading(0)
            my_screen.update()
        distance_x = round((food_x - snake_x) / 20)
        for step in range(distance_x):
            snake.move()
            my_screen.update()
            time.sleep(0.02)
        snake.timmy_head.setheading(270)
        distance_y = round((snake_y - food_y ) / 20)
        for step in range(distance_y):
            snake.move()
            if snake.timmy_head.distance(food) < 10:
                food.create_object()
                snake.plus_snake()
                score.score_add()
            my_screen.update()
            time.sleep(0.02)
    elif food_x <= snake_x and food_y >= snake_y:
        if snake_head == 0:
            snake.timmy_head.setheading(90)
            my_screen.update()
            snake.timmy_head.setheading(180)
            my_screen.update()
        elif snake_head != 0:
            snake.timmy_head.setheading(180)
            my_screen.update()
        distance_x = round((snake_x - food_x) / 20)
        for step in range(distance_x):
            snake.move()
            my_screen.update()
            time.sleep(0.02)
        snake.timmy_head.setheading(90)
        distance_y = round((food_y - snake_y) / 20)
        for step in range(distance_y):
            snake.move()
            if snake.timmy_head.distance(food) < 10:
                food.create_object()
                snake.plus_snake()
                score.score_add()
            my_screen.update()
            time.sleep(0.02)
    elif food_x <= snake_x and food_y <= snake_y:
        if snake_head == 0:
            snake.timmy_head.setheading(90)
            my_screen.update()
            snake.timmy_head.setheading(180)
            my_screen.update()
        elif snake_head != 0:
            snake.timmy_head.setheading(180)
            my_screen.update()
        distance_x = round((snake_x - food_x) / 20)
        for step in range(distance_x):
            snake.move()
            my_screen.update()
            time.sleep(0.02)
        snake.timmy_head.setheading(270)
        distance_y = round((snake_y - food_y) / 20)
        for step in range(distance_y):
            snake.move()
            if snake.timmy_head.distance(food) < 10:
                food.create_object()
                snake.plus_snake()
                score.score_add()
            my_screen.update()
            time.sleep(0.02)



from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score
from game_start import GameStart
from game_input import Game_input

WIDTH = 560
HEIGHT = 560
eat_number = 1

my_screen = Screen()

my_screen.title("Snake game")
my_screen.bgcolor("black")
my_screen.setup(width=WIDTH, height=HEIGHT)
my_screen.tracer(0)


game = Game_input()

game.player()
while game.player_number == 0:
    my_screen.onclick(game.choice_number, btn=1)
    my_screen.update()
game.all_timmy_clear()

game.color_setting()
while game.color == 0:
    my_screen.onclick(game.choice_color, btn=1)
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
snake.color_setting(game.color_choice)
snake.create_snake()

snake_2 = Snake()
snake_2.position()
if game.player_number == 2:
    snake_2.create_snake()

food = Food()
food.create_object()
score = Score()

my_screen.listen()
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.remove_tails, "r")
my_screen.onkey(snake.pause, "space")
my_screen.onkey(snake.robot_pilot, "p")
my_screen.onkey(snake.robot_pilot_2, "l")
my_screen.onkey(snake.mirror, "m")
my_screen.onkey(snake.color, "c")

my_screen.onkey(snake_2.left, "a")
my_screen.onkey(snake_2.right, "d")
my_screen.onkey(snake_2.up, "w")
my_screen.onkey(snake_2.down, "s")
my_screen.onkey(snake_2.remove_tails, "1")
my_screen.onkey(snake_2.pause, "0")
my_screen.onkey(snake_2.robot_pilot, "2")
my_screen.onkey(snake_2.mirror, "3")
my_screen.onkey(snake_2.color, "4")


game_on = True
while game_on:
    my_screen.update()
    time.sleep(game.speed)
    #Pause function both two snake
    if snake.pause_button % 2 == 0 or snake_2.pause_button % 2 == 0:
        while snake.pause_button % 2 == 0 or snake_2.pause_button % 2 == 0:
            time.sleep(1)
            my_screen.update()
    #1. player robot pilots, and move
    if game.player_number == 1:
        if snake.robot_button % 2 == 0 and snake.robot_button_2 % 2 == 0:
            snake.move()
        elif snake.robot_button % 2 != 0:
            robot(snake)
        elif snake.robot_button_2 % 2 != 0:
            robot_2()
    elif game.player_number == 2:
        snake.move()
        snake_2.move()

    #food the snake
    if snake.timmy_head.distance(food) < 10:
        if eat_number % 5 != 0:
            food.create_object()
            snake.plus_snake()
            score.score_add()
            eat_number += 1
        elif eat_number % 5 == 0:
            food.create_object()
            snake.plus_snake()
            score.score_extra_add()
            eat_number += 1
    elif game.player_number == 2 and snake_2.timmy_head.distance(food) < 10:
        if eat_number % 5 != 0:
            food.create_object()
            snake_2.plus_snake()
            score.score_add()
            eat_number += 1
        elif eat_number % 5 == 0:
            food.create_object()
            snake_2.plus_snake()
            score.score_extra_add()
            eat_number += 1
    #bounce with wall
    if game.bounce_wall == 1:
        if game.player_number == 1:
            if abs(snake.timmy_head.xcor()) > (WIDTH/2 - 10) or abs(snake.timmy_head.ycor()) > (WIDTH/2 - 10):
                score.game_over()
                game_on = False
        elif game.player_number == 2:
            if abs(snake.timmy_head.xcor()) > (HEIGHT/2 - 10) or abs(snake.timmy_head.ycor()) > (HEIGHT/2 - 10):
                score.game_over()
                game_on = False
            #2. snake
            if abs(snake_2.timmy_head.xcor()) > (WIDTH/2 - 10) or abs(snake_2.timmy_head.ycor()) > (HEIGHT/2 - 10):
                score.game_over()
                game_on = False
    elif game.bounce_wall == 2:
        if game.player_number == 1:
            if abs(snake.timmy_head.xcor()) > (WIDTH/2 - 10):
                snake.wall_bounce_x()
            elif abs(snake.timmy_head.ycor()) > (HEIGHT/2 - 10):
                snake.wall_bounce_y()
        elif game.player_number == 2:
            if abs(snake.timmy_head.xcor()) > (WIDTH/2 - 20):
                snake.wall_bounce_x()
            elif abs(snake.timmy_head.ycor()) > (HEIGHT/2 - 20):
                snake.wall_bounce_y()
            #2. snake
            if abs(snake_2.timmy_head.xcor()) > (WIDTH / 2 - 20):
                snake_2.wall_bounce_x()
            elif abs(snake_2.timmy_head.ycor()) > (HEIGHT/2 - 20):
                snake_2.wall_bounce_y()

    #collision with own tail
    if game.player_number == 1:
        for timmy in snake.timmy_snake[1:]:
            if snake.timmy_head.distance(timmy) < 10:
                score.game_over()
                game_on = False
    elif game.player_number == 2:
        for timmy in snake.timmy_snake[1:]:
            if snake.timmy_head.distance(timmy) < 10:
                score.game_over()
                game_on = False
        for timmy in snake_2.timmy_snake[1:]:
            if snake_2.timmy_head.distance(timmy) < 10:
                score.game_over()
                game_on = False
        for timmy in snake.timmy_snake[1:]:
            if snake_2.timmy_head.distance(timmy) < 10:
                score.game_over()
                game_on = False
        for timmy in snake_2.timmy_snake[1:]:
            if snake.timmy_head.distance(timmy) < 10:
                score.game_over()
                game_on = False

my_screen.mainloop()





