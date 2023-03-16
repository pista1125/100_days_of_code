#1. turtle, screen
#
from turtle import Turtle, Screen

timmy = Turtle()
# timmy_2 = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("blue")
for n in range(50):
    timmy.forward(100)
    timmy.right(128)
# timmy_2.shape("turtle")
# timmy_2.left(90)
# timmy_2.forward(100)
my_screen = Screen()
print(my_screen.canvheight)

my_screen.exitonclick()


#2. Table from another package
# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
#
# table.align = "l"
#
# print(table)

#3. Coffee maker oop

# from menu import Menu, MenuItem
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine
# # menu = Menu()
# # money = MoneyMachine()
# # coffee = CoffeeMaker()
# #
# #
# # game = True
# # while game:
# #     options = menu.get_items()
# #     choice = input(f"What would you buy? ({options}): ")
# #     if choice == "report":
# #         report_2 = coffee.report()
# #         report_1 = money.report()
# #     elif choice == "off":
# #         game = False
# #     else:
# #         drink = menu.find_drink(choice)
# #         if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
# #             coffee.make_coffee(drink)
#
#
#
#
# #4. Coffee maker. origin verrsion
#
# # from menu import Menu
# # from coffee_maker import CoffeeMaker
# # from money_machine import MoneyMachine
# #
# # money_machine = MoneyMachine()
# # coffee_maker = CoffeeMaker()
# # menu = Menu()
# #
# # is_on = True
# #
# # while is_on:
# #     options = menu.get_items()
# #     choice = input(f"What would you like? ({options}): ")
# #     if choice == "off":
# #         is_on = False
# #     elif choice == "report":
# #         coffee_maker.report()
# #         money_machine.report()
# #     else:
# #         drink = menu.find_drink(choice)
# #
# #         if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
# #             coffee_maker.make_coffee(drink)
#
# #5. My first try in oop
#
# from my_first import My_first_2
#
# coin = My_first_2()
# print(coin.a)
# coin.ubdate_a(4)
# print(coin.a)

#4. Guess a number oop.

#1. Which one greater? my version
from list import data
from list import vs, logo
import random
import pyautogui
# def clear():
#     pyautogui.hotkey("ctrl", "l")
# def pick():
#     return random.choice(data)
#
#
# def check(pick_1, pick_2, choice):
#     if choice == "a":
#         if pick_1["follower_count"] > pick_2["follower_count"]:
#             return True
#         else:
#             return False
#     elif choice == "b":
#         if pick_1["follower_count"] < pick_2["follower_count"]:
#             return True
#         else:
#             return False
#
#
# def game1():
#     pick_2 = pick()
#     should_cont = True
#     score = 0
#     while should_cont:
#         print(logo)
#         pick_1 = pick_2
#         pick_2 = pick()
#         while pick_1 == pick_2:
#             pick_2 = pick()
#         print(f"{pick_1['name']} {pick_1['description']} {pick_1['country']}")
#         print(vs)
#         print(f"{pick_2['name']} {pick_2['description']} {pick_2['country']}")
#         choice = input("Who has more followers? 'A' or 'B' ").lower()
#         checking = check(pick_1, pick_2, choice)
#         clear()
#         if checking == True:
#             score += 1
#             print(f"You're right! Current score: {score}.")
#         elif checking == False:
#             should_cont = False
#             print(f"Sorry, that's wrong. Final score: {score}")
#         else:
#             print("You are stupid.")
#             should_cont = False
#
# game1()