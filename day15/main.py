#1. coffee machine first version
# from list import MENU, resources
# money = 0
#
# def report():
#     print(f"Water: {resources['water']}")
#     print(f"Milk: {resources['milk']}")
#     print(f"Coffee: {resources['coffee']}")
#     print(f"Money: ${money}")
# def insert_money():
#     print("insert a coin")
#     a = float(input("How many quarters?: "))
#     b = float(input("How many dime?: "))
#     c = float(input("How many nickles?: "))
#     d = float(input("How many pennies?:"))
#     coin = a * 0.25 + b * 0.10 + c * 0.05 + d * 0.01
#     return round(coin, 2)
#
#
# def espresso(water, milk, coffee):
#     if water <= resources['water']:
#         a = True
#     elif water > resources['water']:
#         print("I don't have enough water")
#         a = False
#     if milk <= resources['milk']:
#         b = True
#     elif milk > resources['milk']:
#         print("I don't have enough milk")
#         b = False
#     if coffee <= resources['coffee']:
#         c = True
#     elif coffee > resources['coffee']:
#         print("I don't have enough coffee")
#         c = False
#     if a and b and c:
#         return True
#     elif a == False  or b == False or c == False:
#         return False
#
# def game():
#     for _ in range(6):
#         button = input("What would you like to do? ")
#         if button == "espresso":
#             money = insert_money()
#             if money >= MENU['espresso']['cost']:
#                 check = espresso(MENU['espresso']['ingredients']['water'], 0, MENU['espresso']['ingredients']['coffee'] )
#                 if check:
#                     resources["water"] -= MENU['espresso']['ingredients']['water']
#                     resources["coffee"] -= MENU['espresso']['ingredients']['coffee']
#                     change = round(money - MENU['espresso']["cost"], 2)
#                     print(f"Here is your change: {change}")
#                     print("Here is your espresso. Enjoy it.")
#                     money = 0
#             elif money < MENU['espresso']['cost']:
#                 print(f"Sorry, you don't give me enough money, because you gave me {money}")
#         elif button == "latte":
#             money = insert_money()
#             if money >= MENU['latte']['cost']:
#                 check = espresso(MENU['latte']['ingredients']['water'], MENU['latte']['ingredients']['milk'], MENU['latte']['ingredients']['coffee'])
#                 if check:
#                     resources["water"] -= MENU['latte']['ingredients']['water']
#                     resources["milk"] -= MENU['latte']['ingredients']['milk']
#                     resources["coffee"] -= MENU['latte']['ingredients']['coffee']
#                     change = round(money - MENU['espresso']["cost"], 2)
#                     print(f"Here is your change: {change}")
#                     print("Here is your latte. Enjoy it.")
#                     money = 0
#             elif money < MENU['latte']['cost']:
#                 print(f"Sorry, you don't give me enough money, because you gave me {money}")
#         elif button == "cappuccino":
#             money = insert_money()
#             if money >= MENU['cappuccino']['cost']:
#                 check = espresso(MENU['cappuccino']['ingredients']['water'], MENU['cappuccino']['ingredients']['milk'], MENU['cappuccino']['ingredients']['coffee'])
#                 if check:
#                     resources["water"] -= MENU['cappuccino']['ingredients']['water']
#                     resources["milk"] -= MENU['cappuccino']['ingredients']['milk']
#                     resources["coffee"] -= MENU['cappuccino']['ingredients']['coffee']
#                     change = round(money - MENU['cappuccino']["cost"], 2)
#                     print(f"Here is your change: {change}")
#                     print("Here is your cappucino. Enjoy it.")
#                     money = 0
#             elif money < MENU['cappuccino']['cost']:
#                 print(f"Sorry, you don't give me enough money, because you gave me {money}")
#         elif button == "report":
#             report()
#
# game()

#2. turbo version
# from art import logo
# from list import MENU, resources
#
#
# def report():
#     print(f"Water: {resources['water']}")
#     print(f"Milk: {resources['milk']}")
#     print(f"Coffee: {resources['coffee']}")
#     print(f"Profit: ${resources['profit']}")
# def insert_money():
#     print("insert a coin")
#     a = float(input("How many quarters?: "))
#     b = float(input("How many dime?: "))
#     c = float(input("How many nickles?: "))
#     d = float(input("How many pennies?:"))
#     coin = a * 0.25 + b * 0.10 + c * 0.05 + d * 0.01
#     return round(coin, 2)
#
#
# def espresso(water, milk, coffee):
#     if water <= resources['water']:
#         a = True
#     elif water > resources['water']:
#         print("I don't have enough water")
#         a = False
#     if milk <= resources['milk']:
#         b = True
#     elif milk > resources['milk']:
#         print("I don't have enough milk")
#         b = False
#     if coffee <= resources['coffee']:
#         c = True
#     elif coffee > resources['coffee']:
#         print("I don't have enough coffee")
#         c = False
#     if a and b and c:
#         return True
#     elif a == False  or b == False or c == False:
#         return False
#
# def game():
#     print(logo)
#     for _ in range(6):
#         button = input("What would you like to do? ")
#         if button == "report":
#             report()
#         elif button == 'espresso' or button == 'latte' or button == 'cappuccino':
#             money = insert_money()
#             if money >= MENU[button]['cost']:
#                 check = espresso(MENU[button]['ingredients']['water'], MENU[button]['ingredients']['milk'], MENU[button]['ingredients']['coffee'] )
#                 if check:
#                     resources["water"] -= MENU[button]['ingredients']['water']
#                     resources["milk"] -= MENU[button]['ingredients']['milk']
#                     resources["coffee"] -= MENU[button]['ingredients']['coffee']
#                     change = round(money - MENU[button]["cost"], 2)
#                     print(f"Here is your change: {change}")
#                     print(f"Here is your {button}. Enjoy it.")
#                     resources['profit'] += (money - change)
#                     money = 0
#             elif money < MENU[button]['cost']:
#                     print(f"Sorry, you don't give me enough money, because you gave me ${money}, and a {button} is ${MENU[button]['cost']}")
#         else:
#             print("You puss a wrong button")
#
# game()

#3. coffe machine turbo version
from art import logo
from list import MENU, resources, profit


def report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Profit: ${profit['prof']}")


def insert_money():
    print("insert a coin")
    a = float(input("How many quarters?: "))
    b = float(input("How many dime?: "))
    c = float(input("How many nickles?: "))
    d = float(input("How many pennies?:"))
    coin = a * 0.25 + b * 0.10 + c * 0.05 + d * 0.01
    return round(coin, 2)


def checking(button):
    for item in resources:
        if resources[item] < MENU[button]["ingredients"][item]:
            print(f"Sorry don't have enough {item}")
            return False
        else:
            return True

def lost(button):
    for item in resources:
        resources[item] -= MENU[button]['ingredients'][item]


def game():
    print(logo)
    is_game = True
    while is_game:
        button = input("What would you like to do? (espresso/latte/cappuccino): ")
        if button == "report":
            report()
        elif button == "off":
            is_game = False
        elif button == 'espresso' or button == 'latte' or button == 'cappuccino':
            check = checking(button)
            if check:
                money = insert_money()
                if money >= MENU[button]['cost']:
                    lost(button)
                    change = round(money - MENU[button]["cost"], 2)
                    print(f"Here is your change: {change}")
                    print(f"Here is your {button}. Enjoy it.")
                    profit['prof'] += (money - change)
                elif money < MENU[button]['cost']:
                    print(f"Sorry, you don't give me enough money, because you gave me ${money}, and a {button} is ${MENU[button]['cost']}")
        else:
            print("You puss a wrong button")


game()


#4. Coffee machine origin version

# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
#
# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"​Sorry there is not enough {item}.")
#             return False
#     return True
#
#
# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total
#
#
# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
#
#
# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")
#
#
# is_on = True
#
# while is_on:
#     choice = input("What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])

#5. Thinking

# list = ["alfe", 3, 2]
# a = 2
# def what():
#     global a
#     a += 2
#     print(a)
# what()
# print(a)