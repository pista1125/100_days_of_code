import random
from art import logo


cards = [["|A  | ", 11, 1], ["|2  | ", 2, 1], ["|3  | ", 3, 1], ["|4  | ", 4, 1], ["|5  | ", 5, 1], ["|6  | ", 6, 1], ["|7  | ", 7, 1], ["|8  | ", 8, 1], ["|9  | ", 9, 1], ["|10 | ", 10, 1], ["|J  | ", 10, 1], ["|Q  | ", 10, 1], ["|K  | ", 10, 1]]

def kard(player, item):
    h = " ___ "
    j = player
    k = "|(π)|"
    l = "|___|"
    for n in range(item):
        print(h, end=' ')
    print()
    for n in j:
        print(n, end='')
    print()
    for _ in range(item):
        print(k, end=' ')
    print()
    for _ in range(item):
        print(l, end=' ')

def player_game(player, score_player, item):
    choice = random.choice(cards)
    #player += choice[0]
    #score_player += (choice[1])
    #print(f"player card: {player} and the score is {score_player}")
    return choice
def computer_game(computer, score_comp, item):
    comp_choice = random.choice(cards)
    #computer += comp_choice[0]
    #score_comp += comp_choice[1]
    #print(f"computer cards: {computer} and the score is {score_comp}")
    return comp_choice
def black_jack(score_player, player):
    if score_player == 21 and len(player) == 12:
        print("You have a Black Jack. You Win!")
        return 0

def play_game():
    computer = ""
    score_comp = 0
    player = ""
    score_player = 0
    item = 0
    item_comp = 0
    game = True

    a = player_game(player, score_player, item)
    score_player += a[1]
    player += a[0]
    item += a[2]
    print("Player card is")
    kard(player, item)
    print(f"he score is {score_player}")
    b = computer_game(computer, score_comp, item)
    score_comp += b[1]
    computer += b[0]
    item_comp += b[2]
    print("Computer card is")
    kard(computer, item_comp)
    print(f"The score is {score_comp}")
    a = player_game(player, score_player, item)
    score_player += a[1]
    player += a[0]
    item += a[2]
    print("Player card is")
    kard(player, item)
    print(f"The score is {score_player}")
    black_jack(score_player, player)
    if black_jack(score_player, player) == 0:
        game = False
    else:
        cont = input("Do you want more card? ")
    while game:
        if cont == "yes":
            print("Computer card is")
            kard(computer, item_comp)
            print(f"The score is {score_comp}")
            a = player_game(player, score_player, item)
            score_player += a[1]
            player += a[0]
            item += a[2]
            print("Player card is")
            kard(player, item)
            print(f"the score is {score_player}")
            if score_player > 21 and "|A  | " in player:
                player = player.replace("A", "2")
                print(player)
                print(type(player))
                print(len(player))

                score_player -= 9
                print("Player card is")
                kard(player, item)
                print(f"he score is {score_player}")
                cont = input("Do you want more card? ")
            elif score_player > 21:
                print("you lose!")
                game = False
            else:

                cont = input("Do you want more card? ")
        else:
            if score_comp < 17:
                b = computer_game(computer, score_comp, item)
                score_comp += b[1]
                computer += b[0]
                item_comp += 1
            else:
                if score_comp > 21:
                    print("Computer card is")
                    kard(computer, item_comp)
                    print(f"the score is {score_comp}")
                    print("Player card is")
                    kard(player, item)
                    print(f"the score is {score_player}")
                    print("You win")
                    game = False
                elif score_comp == score_player:
                    print("Computer card is")
                    kard(computer, item_comp)
                    print(f"the score is {score_comp}")
                    print("Player card is")
                    kard(player, item)
                    print(f"the score is {score_player}")
                    print("Draw")
                    game = False
                elif score_comp < score_player:
                    print("Computer card is")
                    kard(computer, item_comp)
                    print(f"the score is {score_comp}")
                    print("Player card is")
                    kard(player, item)
                    print(f"the score is {score_player}")
                    print("You win")
                    game = False
                elif score_comp > score_player:
                    print("Computer card is")
                    kard(computer, item_comp)
                    print(f"the score is {score_comp}")
                    print("Player card is")
                    kard(player, item)
                    print(f"the score is {score_player}")
                    print("You lose")
                    game = False
#import pyautogui
play = "yes"
a = 0
while play == "yes":
    if a == 0:
        print(logo)
        play = input("Do you want to play game? ")
        a += 1
    play_game()
    #pyautogui.hotkey("ctrl", "l")
    print(logo)
    play = input("Do you want to play game? ")