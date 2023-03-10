#1. turtle, screen

# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy_2 = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(200)
# timmy_2.shape("turtle")
# timmy_2.left(90)
# timmy_2.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
#
# my_screen.exitonclick()


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

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
money = MoneyMachine()
coffee = CoffeeMaker()


game = True
while game:
    options = menu.get_items()
    choice = input(f"What would you buy? ({options}): ")
    if choice == "report":
        report_2 = coffee.report()
        report_1 = money.report()
    elif choice == "off":
        game = False
    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee.make_coffee(drink)




#4. Coffee maker. origin verrsion

# from menu import Menu
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine
#
# money_machine = MoneyMachine()
# coffee_maker = CoffeeMaker()
# menu = Menu()
#
# is_on = True
#
# while is_on:
#     options = menu.get_items()
#     choice = input(f"What would you like? ({options}): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         coffee_maker.report()
#         money_machine.report()
#     else:
#         drink = menu.find_drink(choice)
#
#         if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
#             coffee_maker.make_coffee(drink)