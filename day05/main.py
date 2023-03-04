#1. practice: loop (for)

# fruits = ["Apple", "Banana", "peach"]
#
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
#     print(fruits)

#2. avarage calculator

# student_heights = input("Input a list of student heights ").split()
#list(range(0, 10))
#[str(x) for x in a]

#student_heights ="1 2 3 4 5".split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
#   print(student_heights)
#
# total_height = 0
# for height in student_heights:
#   total_height += height
# print(total_height)
#
# number_of_student = 0
# for number in student_heights:
#   number_of_student += 1
# print(number_of_student)
#
# avarage = total_height / number_of_student
# print(avarage)

#3.max and min scores

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
#
# maximum_scores = 0
# for score in student_scores:
#     if score > maximum_scores:
#         maximum_scores = score
#     print(maximum_scores)
# print(f"The highest score in the class is: {maximum_scores}")
#
# minimum_scores = maximum_scores
# for score in student_scores:
#     if score < minimum_scores:
#         minimum_scores = score
#     print(minimum_scores)
# print(f"The lowest score in the class is: {minimum_scores}")

#4. range function
# total = 0
# for n in range(0, 101):
#     total += n
# print(total)

#5. add even number

# even_number = 0
# for number in range(0, 101):
#     if number % 2 == 0:
#         even_number += number
# print(even_number)
# #other way
# total = 0
# for number in range(0, 101, 2):
#     total += number
# print(total)

#6. Fizz Buzz

# total = 0
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 != 0:
#         total = "Fizz"
#         print(total)
#     elif number % 5 == 0 and number % 3 != 0:
#         total = "buzz"
#         print(total)
#     elif number % 3 == 0 and number % 5 == 0:
#         total = "FizzBuzz"
#         print(total)
#     else:
#         total = number
#         print(total)
# #other wersion
#
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 ==0:
#         print("Fizz")
#     elif number % 5 ==0:
#         print("Buzz")
#     else:
#         print(number)

#7. Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
#
# password = ""
# for x in range(0, nr_letters):
#     a = letters[random.randint(0, len(letters) - 1)]
#     password += a
#
# for y in range(0, nr_symbols):
#     b = symbols[random.randint(0, len(symbols) - 1)]
#     password += b
#
# for z in range(0, nr_numbers):
#     c = numbers[random.randint(0, len(numbers) - 1)]
#     password += c
#
# print(password)
# Hard Level - Order of characters randomised:
#
# hard_password = list(password)
# final = ""
# for hard in range(0, len(hard_password)):
#     d = hard_password[random.randint(0, len(hard_password) - 1)]
#     final += d
# print(final)

#Other way

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char
print(password)