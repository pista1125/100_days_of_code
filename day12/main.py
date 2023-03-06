#1. Local, Global scope

# enemies = 1
#
# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}") # I can't change a global variable with def

# Local scope

# def drink():
#     potion = 2
#     print(potion)
# drink()
# #print(potion) # I can't call the local scope out of definition

#Global scope

# player = 10
#
# def game():
#     def position():
#         potion = 2
#         print(player)
#
#     position()
# print(player)
# game()

#2. There is no block scope

# game_level = 3
# def crate_ememy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#
#     if game_level < 5:
#         new_enemy = enemies[0]
#
#     print(new_enemy)

#3. How to Modify Variables with Global scope?

# 1 way, that you need to awoid to use
# enemies = 1
#
# def increase_enemies():
#   global enemies
#   enemies += 1
#   print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}") # I can't change a global variable with def

#2. instead use this: Return function

# enemies = 1
# def increase_enemies():
#   print(f"enemies inside function: {enemies}")
#   return enemies + 1
#
#
# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}") # I can't change a global variable with def

#3. Pyton constans and global scope

# PI = 3.1415
# URL = "www.facebook.com"
# def calc():
#     alf = PI + 1
#     print(alf)
#     URL
# calc()

#4. Guess a number project 1. version
# import random
#
# import pyautogui
#
#
#
# def easy_level():
#     a = 1
#     guess = int(input("guess a number: "))
#     while a <= 10:
#         if a == 10:
#             print(f"You lose. The number was {number}.")
#             a += 1
#         elif guess > number:
#             print("This is too hight")
#             guess = int(input("guess a number: "))
#             a += 1
#         elif guess < number:
#             print("This is too low")
#             guess = int(input("guess a number: "))
#             a += 1
#         elif guess == number:
#             print("You guess a number: ")
#             a += 10
#
# def hard_level():
#     a = 1
#     guess = int(input("guess a number: "))
#     while a <= 5:
#         if a == 5:
#             print(f"You lose. The number was {number}.")
#             a += 1
#         elif guess > number:
#             print("This is too hight")
#             guess = int(input("guess a number: "))
#             a += 1
#         elif guess < number:
#             print("This is too low")
#             guess = int(input("guess a number: "))
#             a += 1
#         elif guess == number:
#             print("You guess a number: ")
#             a += 5
# def game():
#     if level == "easy":
#         easy_level()
#     elif level == "hard":
#         hard_level()
# g = "yes"
# while g == "yes":
#     number = random.randint(0, 100)
#     print("you need guess a number beetwen 0 and 100")
#     level = input("choose a level. Type easy or hard: ")
#     game()
#     g = input("Do you want play again? Type yes or no. ")
#     if g == "yes":
#         pyautogui.hotkey("ctrl", "l")

#5. Guess a number 2. version

import random
import pyautogui
def game():
    a = 1
    guess = int(input("guess a number: "))
    while a <= b:
        if a == b:
            print(f"You lose. The number was {number}.")
            a += 1
        elif guess > number:
            print("This is too hight")
            guess = int(input("guess a number: "))
            a += 1
        elif guess < number:
            print("This is too low")
            guess = int(input("guess a number: "))
            a += 1
        elif guess == number:
            print("You guess a number: ")
            a += 10

play = "yes"
while play == "yes":
    number = random.randint(0, 100)
    print("you need guess a number beetwen 0 and 100")
    level = input("choose a level. Type easy or hard: ")
    if level == "easy":
        b = 10
        print("You have 10 guess.")
    elif level == "hard":
        b = 5
        print("You have 5 guess.")
    else:
        print("you write a wrong level. You have 2 guess.")
        b = 2
    game()
    play = input("Do you want play again? Type yes or no. ")
    if play == "yes":
        pyautogui.hotkey("ctrl", "l")
    elif play == "no":
        print("Good bye")
    else:
        print("You are a stupid. You can't, play anymore.")
