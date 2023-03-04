#1. practice
# import random
#
# import my_first_fajl
#
# random_integer = random.randint(0, 10)
# b = my_first_fajl.message + " " + str(my_first_fajl.number)
#
# random_test = random.randint(0, 5) + random.random()
# print(random_test)
# print(b)
# print(random_integer)
# rand_float = random.random()
# print(rand_float)


#2. Heads or Tails

import random

a = random.randint(0, 1)

if a == 1:
    print("Tails")
elif a == 0:
    print("Heads")

#3. List practice
# import random
# state = ["somogy", "baranya", "Tolna", "sopron"]
# number = [1 * 2, 2, 3]
# print(number)
# print(str(state[0]) + str(state[1]))
# a = random.randint(0, 2)
# print(state[a])
#state[0] = "tolna" #csere
# state.append("szeged")
# state.insert(1, "varmegye") #betoldás
# print(state)
#
# print(len(number))
# a = str(12334)
# print(len(a))

#4. Banker Roulette

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

a = len(names)
random_choice = random.randint(0, a-1)
name_who_pay = names[random_choice]

print(name_who_pay + " is going to pay the bill")

#5. lists fusion

# fruit = ["Strawberries", "spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries"]
# vegetables = ["Avocados", "Sweet corn", "Pineapples", "Cabbages", "Onions", "Sweet peas, (frozen)", "Papayas"]
#
# dirty_dozen = [fruit, vegetables]
#
# print(dirty_dozen)
#
# print(dirty_dozen[0])
# print(dirty_dozen[1][2])
#
# fruit[0] = "melons"  #replace
# print(fruit)

#6. Treasure map

# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")

#position = list(position)

# a = int(position[0])
# b = int(position[1])
#
# map[b-1][a-1] = "x"
#
# print(f"{row1}\n{row2}\n{row3}")

#7. Rock paper scissors

# import random
#
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# # The mistake solved
# player_number = -1
# while 0 > player_number or player_number > 2:
#     try:
#         player_number = int(input("Which one do you want chooce? 0 for Rock, 1 for Paper, 2 for scissors\n"))
#     except:
#         print("please write a number")
# player_number = int(input("Which one do you want chooce? 0 for Rock, 1 for Paper, 2 for scissors\n"))
# computer_number = random.randint(0, 2)
#
# game_images = [rock, paper, scissors]
# game_images_name = ["Rock", "Paper", "Scissors"]
# if 0 <= player_number <= 2:
#     print(f"Player chooce: {game_images_name[player_number]} {game_images[player_number]}")
# print(f"Computer chooce: {game_images_name[computer_number]} {game_images[computer_number]}")
#
# if (player_number == 0 and computer_number == 2) or (player_number == 1 and computer_number == 0) or (player_number == 2 and computer_number == 1):
#     print("You Win")
# elif (player_number == 0 and computer_number == 1) or (player_number == 1 and computer_number == 2) or (player_number == 2 and computer_number == 0):
#     print("You Lose")
# elif (player_number == 0 and computer_number == 0) or (player_number == 1 and computer_number == 1) or (player_number == 2 and computer_number == 2):
#     print("Draw")
# elif player_number > 2 or player_number < 0:
#     print("You typed wrong number. You Lose")

# other way the picture
# if player_number == 0:
#     print(f"Player choose: Rock\n {rock}")
# elif player_number == 1:
#     print(f"Player choose: Paper\n {paper}")
# elif player_number == 2:
#     print(f"Player choose: Scissors\n {scissors}")
#
# if computer_number == 0:
#     print(f"Computer choose: Rock\n {rock}")
# elif computer_number == 1:
#     print(f"Computer choose: Paper\n {paper}")
# elif computer_number == 2:
#     print(f"Computer choose: Scissors\n {scissors}")


