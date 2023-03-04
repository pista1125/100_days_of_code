#1. Black jack project
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
from art import logo
def player_game(player, score_player):
    choice = random.choice(cards)
    score_player += choice
    player.append(choice)
    #print(f"player card: {player} and the score is {score_player}")
    return score_player
def computer_game(computer, score_comp):
    comp_choice = random.choice(cards)
    computer.append(comp_choice)
    score_comp += comp_choice
    #print(f"computer cards: {computer} and the score is {score_comp}")
    return score_comp
def black_jack(score_player, player):
    if score_player == 21 and len(player) == 2:
        print("You have a Black Jack. You Win!")
        return 0

def play_game():
    computer = []
    score_comp = 0
    player = []
    score_player = 0
    game = True

    score_player = player_game(player, score_player)
    print(f"player card: {player} and the score is {score_player}")
    score_comp = computer_game(computer, score_comp)
    print(f"computer cards: {computer} and the score is {score_comp}")
    score_player = player_game(player, score_player)
    print(f"player card: {player} and the score is {score_player}")
    black_jack(score_player, player)
    if black_jack(score_player, player) == 0:
        game = False
    else:
        cont = input("Do you want more card? ")
    while game:
        if cont == "yes":
            print(f"computer cards: {computer} and the score is {score_comp}")
            score_player = player_game(player, score_player)
            print(f"player card: {player} and the score is {score_player}")
            if score_player > 21 and 11 in player:
                player.remove(11)
                player.append(1)
                score_player = sum(player)
                print(f"player card: {player} and the score is {score_player}")
                cont = input("Do you want more card? ")
            elif score_player > 21:
                print("you lose!")
                game = False
            else:
                cont = input("Do you want more card? ")

        else:
            if score_comp < 17:
                score_comp = computer_game(computer, score_comp)
            else:
                if score_comp > 21:
                    print(f"computer cards: {computer} and the score is {score_comp}")
                    print(f"player card: {player} and the score is {score_player}")
                    print("You win")
                    game = False
                elif score_comp == score_player:
                    print(f"computer cards: {computer} and the score is {score_comp}")
                    print(f"player card: {player} and the score is {score_player}")
                    print("Draw")
                    game = False
                elif score_comp < score_player:
                    print(f"computer cards: {computer} and the score is {score_comp}")
                    print(f"player card: {player} and the score is {score_player}")
                    print("You win")
                    game = False
                elif score_comp > score_player:
                    print(f"computer cards: {computer} and the score is {score_comp}")
                    print(f"player card: {player} and the score is {score_player}")
                    print("You lose")
                    game = False

play = "yes"
a = 0
while play == "yes":
    if a == 0:
        print(logo)
        play = input("Do you want to play game? ")
        a += 1
    play_game()
    print(logo)
    play = input("Do you want to play game? ")

#2. Black jack origin version

# import random
# from art import logo
#
# def deal_card():
#   """Returns a random card from the deck."""
#   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#   card = random.choice(cards)
#   return card
#
# def calculate_score(cards):
#   """Take a list of cards and return the score calculated from the cards"""
#   if sum(cards) == 21 and len(cards) == 2:
#     return 0
#   if 11 in cards and sum(cards) > 21:
#     cards.remove(11)
#     cards.append(1)
#   return sum(cards)
#
# def compare(user_score, computer_score):
#   #Bug fix. If you and the computer are both over, you lose.
#   if user_score > 21 and computer_score > 21:
#     return "You went over. You lose 😤"
#   if user_score == computer_score:
#     return "Draw 🙃"
#   elif computer_score == 0:
#     return "Lose, opponent has Blackjack 😱"
#   elif user_score == 0:
#     return "Win with a Blackjack 😎"
#   elif user_score > 21:
#     return "You went over. You lose 😭"
#   elif computer_score > 21:
#     return "Opponent went over. You win 😁"
#   elif user_score > computer_score:
#     return "You win 😃"
#   else:
#     return "You lose 😤"
#
# def play_game():
#   print(logo)
#   user_cards = []
#   computer_cards = []
#   is_game_over = False
#
#   for _ in range(2):
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card())
#
#   while not is_game_over:
#     user_score = calculate_score(user_cards)
#     computer_score = calculate_score(computer_cards)
#     print(f"   Your cards: {user_cards}, current score: {user_score}")
#     print(f"   Computer's first card: {computer_cards[0]}")
#
#     if user_score == 0 or computer_score == 0 or user_score > 21:
#       is_game_over = True
#     else:
#       user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#       if user_should_deal == "y":
#         user_cards.append(deal_card())
#       else:
#         is_game_over = True
#
#   while computer_score != 0 and computer_score < 17:
#     computer_cards.append(deal_card())
#     computer_score = calculate_score(computer_cards)
#
#   print(f"   Your final hand: {user_cards}, final score: {user_score}")
#   print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
#   print(compare(user_score, computer_score))
#
# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
#   play_game()

