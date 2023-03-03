#1. Black jack project
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def player_game(player, score_player):
    choice = random.choice(cards)
    score_player += choice
    player += str(choice)
    print(f"player card: {player} and the score is {score_player}")
    return score_player
def computer_game(computer, score_comp):
    comp_choice = random.choice(cards)
    computer += str(comp_choice)
    score_comp += comp_choice
    print(f"computer cards: {computer} and the score is {score_comp}")
    return score_comp

computer = []
score_comp = 0
player = []
score_player = 0

game = input("Do you want to play game?")
if game == "yes":
    game = True
else:
    game = False
while game:
    score_player = player_game(player, score_player)
    score_comp = computer_game(computer, score_comp)
    score_player = player_game(player, score_player)
    cont = input("Do you want more card? ")
    if cont == "yes":
        print(f"computer cards: {computer} and the score is {score_comp}")
        score_player = player_game(player, score_player)
        if score_player > 21:
            print("you lose!")
            game = False
        else:
            cont = input("Do you want more card? ")

    else:
        score_comp = computer_game(computer, score_comp)
        print(f"player card: {player} and the score is {score_player}")
        if score_comp < 17:
            score_comp = computer_game(computer, score_comp)
            print(f"player card: {player} and the score is {score_player}")
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