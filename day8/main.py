#1. Function

# def greet():
#     print("Hello")
#     print("How do You do?")
#     print("isn't weather nice today?")
#
# greet()

#2. Function with variable

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do You do? {name}")
#
# greet_with_name("Istvan")

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do You do? {name}")
# apple = input("What is your name? ")
#
# greet_with_name(apple)

#3. Function with more than 1 imput

# def greet_with_name(name, location):
#     print(f"Hello {name}")
#     print(f"I am living in {location}")
# n = input("What is your name? ")
# l = input("where do you live? ")
# greet_with_name(name=n, location=l)

#4. challange

#Write your code below this line 👇

# import math
# def paint_calc(height, width, cover):
#     number = math.ceil(height * width / cover)
#     print(f"You'll need {number} cans of paint.")
#
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


#5. Prime number checker my version

# number = int(input("check this number: "))
# def check(number):
#     switch = "false"
#     for c in range(2, number):
#         if number % c == 0:
#             switch = "true"
#     if switch == "true":
#         print("This is not a prime number")
#     elif switch == "false":
#         print("This is a prime number")
# check(number = number)

#6. Misi version prime check

# number = int(input("check this number: "))
# def check(number):
#     for c in range(2, number):
#         #print(c)
#         if number % c == 0:
#             return False
#     return True
# print(check(number = 97))
# print(check(number = 5))
# print(check(number = 4))

# for x in range(2, 101):
#     if check(x):
#         print(f"{x} prim number")
#     else:
#         print(f"{x} not a prim")

#7. Other version

# def check(number):
#     is_prime = True
#     for c in range(2, number):
#         if number % c == 0:
#             is_prime = False
#     if is_prime:
#         print("This is a prime number")
#     else:
#         print("This is mot a prime number")
#
# n = int(input("check this number: "))
# check(number = n)

#8. Ceaser chipher my version

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# game = "yes"
# while game == "yes":
#     switch = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     if switch == "encode":
#         def chiper(shift):
#             chiper_word = ""
#             for n in word:
#                 for x in range(0, len(letters)):
#                     if n == letters[x]:
#                         chiper_word += letters[x + shift]
#             print(f"Your chiper word is {chiper_word}")
#
#         word = input("write your word here\n").lower()
#         number = int(input("Please write a shift number\n"))
#         chiper(number)
#         game = input("Type 'yes' if you want again otherwise 'no'\n")
#     elif switch == "decode":
#         def chiper(shift):
#             chiper_word = ""
#             for n in word:
#                 for x in range(0, len(letters)):
#                     if n == letters[x]:
#                         chiper_word += letters[x - shift]
#             print(chiper_word)
#
#         word = input("write your word here\n").lower()
#         number = int(input("Please write a shift number\n"))
#         chiper(number)
#         game = input("Type 'yes' if you want again otherwise 'no'\n")

#9. Ceaser chipher my version turbo edition
#
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# def chiper(word, shift):
#     chiper_word = ""
#     for n in word:
#         if n in letters:
#             position = letters.index(n)
#             new_position = position + shift
#             x = letters[new_position]
#             chiper_word += x
#         else:
#             chiper_word += n
#     print(f"Your chiper word is {chiper_word}")
#
# def de_chiper(de_word, shift):
#     chiper_word = ""
#     for n in de_word:
#         if n in letters:
#             position = letters.index(n)
#             new_position = position - shift
#             x = letters[new_position]
#             chiper_word += x
#         else:
#             chiper_word += n
#     print(f" Your message was {chiper_word}")
# from art import logo
# print(logo)
# game = True
# while game:
#     switch = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     if switch == "encode":
#         w = input("write your word here\n").lower()
#         n = int(input("Please write a shift number\n"))
#         n = n % 26
#         chiper(shift=n, word=w)
#         game = input("Type 'yes' if you want again otherwise 'no'\n")
#     elif switch == "decode":
#         w = input("write your word here\n").lower()
#         n = int(input("Please write a shift number\n"))
#         n = n % 26
#         de_chiper(de_word=w, shift=n)
#         game = input("Type 'yes' if you want again otherwise 'no'\n")
#     else:
#         game = input("Type 'yes' if you want again otherwise 'no'\n")
#     if game == "yes":
#         game = True
#     elif game == "no":
#         game = False
#         print("Goodbye")
#     else:
#         game = False
#         print("You are a stupid. You can't play game anymore!")

#10. original first step
#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
#
# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     new_letter = alphabet[new_position]
#     cipher_text += new_letter
#   print(f"The encoded text is {cipher_text}")
#
# encrypt(plain_text=text, shift_amount=shift)

#11. step two

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")
#
# def decrypt(cipher_text, shift_amount):
#   plain_text = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_amount
#     plain_text += alphabet[new_position]
#   print(f"The decoded text is {plain_text}")
#
# if direction == "encode":
#   encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#   decrypt(cipher_text=text, shift_amount=shift)

#12. step three

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#       shift_amount *= -1
#   for letter in start_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     end_text += alphabet[new_position]
#   print(f"Here's the {direction}d result: {end_text}")
#
# caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

#13. Finish code

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

from art import logo
print(logo)

should_end = False
while not should_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")
print("hello")