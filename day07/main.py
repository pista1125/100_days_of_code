#1. Hangman first step
# import random
# world_list = ["ardvark", "baboon", "camel"]
#
#
# letter = input("guess a letter: ").lower()
#
# world = random.choice(world_list)
#
# world = list(world)
# #print(len(world) * "_")
#
# for n in world:
#     if letter == n:
#         print("Right")
#     elif letter != n:
#         print("wrong")
#2. Hangman step two
# import random
# world_list = ["ardvark", "baboon", "camel"]
#
#
# guess = input("guess a letter: ").lower()
#
# chosen_world = random.choice(world_list)
#
# #chosen_world = list(chosen_world)
# display =list(len(chosen_world) * "_")
# #other wersion
# # display = []
# # for _ in world:
# #     display += "_"
# # print(display)
# print(chosen_world)
# print(display)
#
# for position in range(len(chosen_world)):
#     letter = chosen_world[position]
#     if letter == guess:
#         display[position] = letter
# print(display)


#3. step three
# import random
# world_list = ["ardvark", "baboon", "camel"]
# chosen_world = random.choice(world_list)
# #chosen_world = list(chosen_world)
# display =list(len(chosen_world) * "_")
#
#
# #other wersion
# # display = []
# # for _ in world:
# #     display += "_"
# # print(display)
# print(chosen_world)
# print(display)
#
# end_of_game = True
# while end_of_game:
#     guess = input("guess a letter: ").lower()
#     for position in range(len(chosen_world)):
#         letter = chosen_world[position]
#         if letter == guess:
#             display[position] = letter
#     print(display)
#     if "_" not in display:
#         end_of_game = False
#         print("You Win")

#4. step four
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
# import random
# world_list = ["ardvark", "baboon", "camel"]
# chosen_world = random.choice(world_list)
# #chosen_world = list(chosen_world)
# display =list(len(chosen_world) * "_")
#
#
# #other wersion
# # display = []
# # for _ in world:
# #     display += "_"
# # print(display)
# print(chosen_world)
# print(display)
# lives = 6
# end_of_game = True
# while end_of_game:
#     guess = input("guess a letter: ").lower()
#     for position in range(len(chosen_world)):
#         letter = chosen_world[position]
#         if letter == guess:
#             display[position] = letter
#     print(display)
#     if guess not in chosen_world:
#         lives -= 1
#         if lives == 0:
#             end_of_game = False
#             print("You lose")
#         print(stages[lives])
#     if "_" not in display:
#         end_of_game = False
#         print("You Win")

#5. Final version
import random
import hangman_word
import logo
from replit import clear

world_list = hangman_word.word_list
chosen_world = random.choice(world_list)
display = list(len(chosen_world) * "_")
print(logo.logo)
print(''.join(display))
lives = 6
end_of_game = True
while end_of_game:
    guess = input("guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(len(chosen_world)):
        letter = chosen_world[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_world:
        lives -= 1
        if lives == 0:
            end_of_game = False
            print(f"You lose, because the word was {chosen_world}")
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(logo.stages[lives])
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = False
        print("You Win")
