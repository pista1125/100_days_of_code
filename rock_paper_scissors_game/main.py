from tkinter import *
import random
option = ["Rock", "Paper", "Scissors"]
Font = ("Courier", 20, "bold")
comp_choice = None
play_choice = None
who_win = None
player_win = 0

def player_label():
    play_lab_1 = Label(text="Your choice is", font=Font)
    play_lab_1.grid(column=0, row= 3)

    play_lab = Label(text=play_choice, font=Font)
    play_lab.grid(column=0, row=4)

def computer_label():
    computer_label_1 = Label(text="Computer choice is", font=Font)
    computer_label_1.grid(row=3, column=2, pady=20)
    computer_label = Label(text=comp_choice, font=Font)
    computer_label.grid(row=4, column=2, pady=20)

def rock():
    global comp_choice
    global play_choice
    play_choice = "Rock"
    comp_choice = random.choice(option)
    player_label()
    computer_label()
    game()
    new_game()

def paper():
    global comp_choice
    global play_choice
    play_choice = "Paper"
    comp_choice = random.choice(option)
    player_label()
    computer_label()
    game()
    new_game()

def scissors():
    global comp_choice
    global play_choice
    play_choice = "Scissors"
    comp_choice = random.choice(option)
    player_label()
    computer_label()
    game()
    new_game()


def game():
    global who_win
    global player_win
    if comp_choice == "Rock" and play_choice == "Rock" or comp_choice == "Paper" and play_choice == "Paper" or comp_choice == "Scissors" and play_choice == "Scissors":
        who_win = "Draw"
    elif comp_choice == "Rock" and play_choice == "Paper" or comp_choice == "Paper" and play_choice == "Scissors" or comp_choice == "Scissors" and play_choice == "Rock":
        who_win = "You win"
        player_win += 1
    elif comp_choice == "Rock" and play_choice == "Scissors" or comp_choice == "Paper" and play_choice == "Rock" or comp_choice == "Scissors" and play_choice == "Paper":
        who_win = "You Lose"

    win_label = Label(text=who_win, font=Font)
    win_label.grid(row=5, column=1)


def new_game():
    want_play_again_label = Label(text="Do you want play again?", font=Font)
    want_play_again_label.grid(row=6, column=1, pady=20)

    want_play_again_button_1 = Button(text="Yes", font=Font)
    want_play_again_button_1.grid(row=7, column=0)

    want_play_again_button_2 = Button(text="No", font=Font)
    want_play_again_button_2.grid(row=7, column=2)


my_window = Tk()
my_window.title("Rock, Paper, Scissors")
my_window.config(padx=50, pady=50, bg="blue")

#Label

tittle_label = Label(text="Rock, Paper, Scissors Game", font=Font, fg="yellow", bg="blue", highlightthickness=0)
tittle_label.grid(row=0, column=1)

choice_label = Label(text="Choice one button", font=Font, bg="blue")
choice_label.grid(row=1, column=1, pady=20)

rock_button = Button(text="Rock", command=rock, font=Font, )
rock_button.grid(row=2, column=0)

paper_button = Button(text="Paper", command=paper, font=Font)
paper_button.grid(row=2, column=1)

scissors_button = Button(text="Scissors", command=scissors, font=Font)
scissors_button.grid(row=2, column=2)



my_window.mainloop()