#1. my game first version
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

from list import MENU, resources
money = 0

def report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${money}")
def insert_money():
    print("insert a coin")
    a = float(input("How many quarters?: "))
    b = float(input("How many dime?: "))
    c = float(input("How many nickles?: "))
    d = float(input("How many pennies?:"))
    coin = a * 0.25 + b * 0.10 + c * 0.05 + d * 0.01
    return round(coin, 2)


def espresso(water, milk, coffee):
    if water <= resources['water']:
        a = True
    elif water > resources['water']:
        print("I don't have enough water")
        a = False
    if milk <= resources['milk']:
        b = True
    elif milk > resources['milk']:
        print("I don't have enough milk")
        b = False
    if coffee <= resources['coffee']:
        c = True
    elif coffee > resources['coffee']:
        print("I don't have enough coffee")
        c = False
    if a and b and c:
        return True
    elif a == False  or b == False or c == False:
        return False

def game():
    for _ in range(6):
        button = input("What would you like to do? ")
        if button == "report":
            report()
        elif button == 'espresso' or button == 'latte' or button == 'cappuccino':
            money = insert_money()
            if money >= MENU[button]['cost']:
                check = espresso(MENU[button]['ingredients']['water'], 0, MENU[button]['ingredients']['coffee'] )
                if check:
                    resources["water"] -= MENU[button]['ingredients']['water']
                    resources["coffee"] -= MENU[button]['ingredients']['coffee']
                    change = round(money - MENU[button]["cost"], 2)
                    print(f"Here is your change: {change}")
                    print(f"Here is your {button}. Enjoy it.")
                    money = 0
            elif money < MENU[button]['cost']:
                    print(f"Sorry, you don't give me enough money, because you gave me ${money}, and a {button} is ${MENU[button]['cost']}")
        else:
            print("You puss a wrong button")

game()