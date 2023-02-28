#1. project: ride?

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height > 120:
#     print("can ride")
# else:
#     print("can't ride")

#2. project: even-odd number

# number = int(input("Which number do you want to check? "))
#
# number_1 = number % 2
#
# if number_1 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")

#3. project: ride?

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height > 120:
#     print("can ride")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("need pay $5")
#     elif age <= 18:
#         print("need pay $7")
#     else:
#         print("need pay $12")
# else:
#     print("can't ride")

#4. BMI calculator turbo version

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
#
# bmi = round(weight / (height ** 2))

# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese")

#5. Leap or not?

# year = int(input("Which year do you want to check? "))
#
# if year % 4 != 0:
#     print("Not leap year.")
# else:
#     if year % 100 !=0:
#         print("Leap year.")
#     else:
#         if year % 400 !=0:
#             print("Not leap year.")
#         else:
#             print("Leap year.")

#6. Ride or not + photo or not?

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height > 120:
#     print("can ride")
#     age = int(input("What is your age? "))
#     bill = 0
#     if age < 12:
#         bill = 5
#         print(f"need pay ${bill}")
#     elif age <= 18:
#         bill = 7
#         print(f"need pay ${bill}")
#     else:
#         bill = 12
#         print(f"need pay ${bill}")
#     photo = input("Do you want a photos? yes or no? ")
#     if photo == "yes":
#         bill += 3
#     print(f"you need pay: ${bill}")
# else:
#     print("can't ride")

#7. Pizza order

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
#
# if size == "S":
#     price = 15
#     if add_pepperoni == "Y":
#         price += 2
# elif size == "M":
#     price = 20
#     if add_pepperoni == "Y":
#         price += 3
# elif size == "L":
#     price = 25
#     if add_pepperoni == "Y":
#         price += 3
# if extra_cheese == "Y":
#     price += 1

# print(f"Your final bill is: {price}.")

#I can write a code separate:

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
#
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill == 25
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
# if extra_cheese == "Y":
#     bill += 1
# print(f"Your final bill is ${bill}.")

#8. Ride or not + photo or not? + extra

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height > 120:
#     print("can ride")
#     age = int(input("What is your age? "))
#     bill = 0
#     if age < 12:
#         bill = 5
#         print(f"need pay ${bill}")
#     elif age <= 18:
#         bill = 7
#         print(f"need pay ${bill}")
#     elif age > 45 and age < 55:
#         bill = 0
#         print(f"need pay ${bill}")
#     else:
#         bill = 12
#         print(f"need pay ${bill}")
#     photo = input("Do you want a photos? yes or no? ")
#     if photo == "yes":
#         bill += 3
#     print(f"you need pay: ${bill}")
# else:
#     print("can't ride")

#9. True Love?

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
#
# name1_lower = name1.lower()
# name2_lower = name2.lower()
#
# true = name1_lower.count("t") + name1_lower.count("r") + name1_lower.count("u") + name1_lower.count("e")
# true_1 = name2_lower.count("t") + name2_lower.count("r") + name2_lower.count("u") + name2_lower.count("e")
#
# a = true + true_1
#
# love = name1_lower.count("l") + name1_lower.count("o") + name1_lower.count("v") + name1_lower.count("e")
# love_1 = name2_lower.count("l") + name2_lower.count("o") + name2_lower.count("v") + name2_lower.count("e")
#
# b = love + love_1
#
# score = int(str(a) + str(b))
# if score < 10 or score > 90:
#     print(f" Your score is {score}, you go together like coke and mentos.")
# elif 40 < score < 50:
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"your score is {score}")

# other version:

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
#
# name = name1 + name2
# name_lower = name.lower()
#
# t = name_lower.count("t")
# r = name_lower.count("r")
# u = name_lower.count("u")
# e = name_lower.count("e")
#
# true = t + r + u + e
#
# l = name_lower.count("l")
# o = name_lower.count("o")
# v = name_lower.count("v")
# e = name_lower.count("e")
#
# love = l + o + v + e
#
# score = int(str(true) + str(love))
# if score < 10 or score > 90:
#     print(f" Your score is {score}, you go together like coke and mentos.")
# elif 40 < score < 50:
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"your score is {score}")


#10. Find a treasure

# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/[TomekK]
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
#
# choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
# if choice1 == "left":
#   choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
#   if choice2 == "wait":
#     choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
#     if choice3 == "red":
#       print("It's a room full of fire. Game Over.")
#     elif choice3 == "yellow":
#       print("You found the treasure! You Win!")
#     elif choice3 == "blue":
#       print("You enter a room of beasts. Game Over.")
#     else:
#       print("You chose a door that doesn't exist. Game Over.")
#   else:
#     print("You get attacked by an angry trout. Game Over.")
# else:
#   print("You fell into a hole. Game Over.")