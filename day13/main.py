#1. Debuging the next few program.
############DEBUGGING#####################

# Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()
#range function don't use the last number. Therefore you will not see anything.

# Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])
# #random function use the last number as well. But the list count start from 0. So the dice_ings include 0- 5 items

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
# #1994 don't understand. Need a = wherever.

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")
# #need a f string, and indentation, and the imput need transformation from str to int.

#Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# #in Word_per_page line you don't need a duble = because you just wanted to set the variable, not to check


# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)
#
# mutate([1,2,3,5,8,13])
# you need indented a b_list line to for ciklus.