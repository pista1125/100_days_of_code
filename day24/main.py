#1. Snake game

# from turtle import Screen
# import time
# from snake import Snake
# from food import Food
# from score import Score
#
# my_screen = Screen()
#
# my_screen.setup(width=560, height=560)
# my_screen.bgcolor("black")
# my_screen.title("My snake game")
# my_screen.tracer(0)
#
# snake = Snake()
# food = Food()
# score = Score()
#
# my_screen.listen()
# my_screen.onkey(snake.left, "Left")
# my_screen.onkey(snake.right, "Right")
# my_screen.onkey(snake.up, "Up")
# my_screen.onkey(snake.down, "Down")
#
#
# game_on = True
# while game_on:
#     my_screen.update()
#     time.sleep(0.1)
#     snake.move()
#     if snake.timmy_head.distance(food) < 10:
#         food.create_object()
#         snake.plus_snake()
#         score.score_add()
#
#     if snake.timmy_head.xcor() > 280 or snake.timmy_head.xcor() < -280 or snake.timmy_head.ycor() > 280 or snake.timmy_head.ycor() < -280:
#         score.reset()
#         snake.reset()
#
#     for timmy in snake.timmy_snake[1:]:
#         if snake.timmy_head.distance(timmy) < 10:
#             score.reset()
#             snake.reset()
#
# my_screen.exitonclick()


#2. open and read file


# file = open("my_file.txt")
#
# content = file.read()
# print(content)
#
# file.close()

#3. open and read file another way

# with open("my_file.txt") as file:
#
#     content = file.read()
#     print(content)

#4. open and write file

# with open("my_file.txt", mode="w") as file:
#     file.write("no way")

#5. open and add file

# with open("my_file.txt", mode="a") as file:
#     file.write("\nno way")

#6. Create new file and add text (It's working with Write mode)

# with open("my_new_file.txt", mode="w") as file:
#     file.write("\nHello, I'm here")


#7. find and use file in another folders
#absolut file found
# with open("/Users/Istvan/Desktop/my_file.txt") as data:
#     file = data.read()
#     print(file)

#relative file found
# with open("../../../../Istvan/Desktop/my_file.txt") as data:
#     file = data.read()
#     print(file)


#8. Letter generate from txt file


# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contants = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contants.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)