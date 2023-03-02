#1. Function with output

# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
#
# name = input("What is your first name? ")
# name_2 = input("What is your last name? ")
#
# # print(format_name(name, name_2))
# #other way:
# output = format_name(name, name_2)
# print(output)

#2. Return function

# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You are stupid"
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
#
# name = input("What is your first name? ")
# name_2 = input("What is your last name? ")
#
# print(format_name(name, name_2))

#3. code challange

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# def days_in_month(year,month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year):
#         month_days[1] += 1
#     return month_days[month - 1]
# # 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(f"This month is {days}")

#4. Return function with name

# def format_name(f_name, l_name):
#     ''' My first function with name'''
#     if f_name == "" or l_name == "":
#         return "You are stupid"
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"


# name = input("What is your first name? ")
# name_2 = input("What is your last name? ")
#
# print(format_name(name, name_2))

#5. Calculator my version
# from symbol import symbol
# from symbol import calculator_symbol
# def calculator(first_number, operation, next_number):
#     if operation == "+":
#         a = first_number + next_number
#         print(f"{first_number} + {next_number} = {a}")
#         return a
#     elif operation == "-":
#         a = first_number - next_number
#         print(f"{first_number} - {next_number} = {a}")
#         return a
#     elif operation == "*":
#         a = first_number * next_number
#         print(f"{first_number} * {next_number} = {a}")
#         return a
#     elif operation == "/":
#         a = first_number / next_number
#         print(f"{first_number} / {next_number} = {a}")
#         return a
#
# print(calculator_symbol)
# first_number = float(input("What's the first number?: "))
# print(symbol)
# game = "yes"
# while game == "yes":
#     operation = input("Pick an operation: ")
#     next_number = float(input("What's the next number: "))
#     b = calculator(first_number, operation, next_number)
#     game = input(f"Do you want continue calculator with {b}?\n Type 'yes' or 'no'")
#     if game == "yes":
#         operation = input("Pick an operation: ")
#         next_number = float(input("What's the next number: "))
#         calculator(b, operation, next_number)
#         game = input(f"Do you want continue calculator with {b}?\n Type 'yes' or 'no'")
#     elif game == "no":
#         first_number = float(input("What's the first number?: "))
#         operation = input("Pick an operation: ")
#         next_number = float(input("What's the next number: "))
#         c = calculator(first_number, operation, next_number)
#         game = input(f"Do you want continue calculator with {c}?\n Type 'yes' or 'no'")
#     else:
#         game = "no"

#6. Calculator Origin
# def add(n1, n2):
#     return n1 + n2
# def subtract(n1, n2):
#     return n1 - n2
# def multiply(n1, n2):
#     return n1 * n2
# def divide(n1, n2):
#     return n1 / n2
# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide
# }
# def calculator():
#     num1 = float(input("What's the first number?: "))
#     for symbol in operations:
#         print(symbol)
#     should_continue = True
#     while should_continue:
#         operation_symbol = input("Pick an operation: ")
#         num2 = float(input("What's the next number?: "))
#         calculation_function = operations[operation_symbol]
#         answer = calculation_function(num1, num2)
#         print(f"{num1} {operation_symbol} {num2} = {answer}")
#
#         if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
#             num1 = answer
#         else:
#             should_continue = False
#             calculator()
#
# calculator()
