from tkinter import *
import random
option = ["Rock", "Paper", "Scissors"]
Font = ("Courier", 20, "bold")
comp_choice = None
play_choice = None
who_win = None
player_win = 0
game_number = 0

def player_label():
    play_lab_1 = Label(text="Your choice is", font=Font)
    play_lab_1.grid(column=0, row= 3)

    play_lab.config(text=play_choice)



def computer_label():
    computer_label_1 = Label(text="Computer choice is", font=Font)
    computer_label_1.grid(row=3, column=2, pady=20)

    computer_label_thing.config(text=comp_choice)
    if comp_choice == "Rock":
        canvas_2.itemconfig(computer_image, image=rock_img)
    elif comp_choice == "Scissors":
        canvas_2.itemconfig(computer_image, image=scissor_img)
    elif comp_choice == "Paper":
        canvas_2.itemconfig(computer_image, image=paper_img)



def rock():
    global comp_choice
    global play_choice
    play_choice = "Rock"
    comp_choice = random.choice(option)
    canvas.itemconfig(player_image, image=rock_img)
    player_label()
    computer_label()
    game()
    new_game()

def paper():
    global comp_choice
    global play_choice
    play_choice = "Paper"
    comp_choice = random.choice(option)
    canvas.itemconfig(player_image, image=paper_img)
    player_label()
    computer_label()
    game()
    new_game()

def scissors():
    global comp_choice
    global play_choice
    play_choice = "Scissors"
    comp_choice = random.choice(option)
    canvas.itemconfig(player_image, image=scissor_img)
    player_label()
    computer_label()
    game()
    new_game()


def game():
    global who_win
    global player_win
    global game_number
    if comp_choice == "Rock" and play_choice == "Rock" or comp_choice == "Paper" and play_choice == "Paper" or comp_choice == "Scissors" and play_choice == "Scissors":
        who_win = "Draw"
        game_number += 1
    elif comp_choice == "Rock" and play_choice == "Paper" or comp_choice == "Paper" and play_choice == "Scissors" or comp_choice == "Scissors" and play_choice == "Rock":
        who_win = "You win"
        game_number += 1
        player_win += 1
    elif comp_choice == "Rock" and play_choice == "Scissors" or comp_choice == "Paper" and play_choice == "Rock" or comp_choice == "Scissors" and play_choice == "Paper":
        who_win = "You Lose"
        game_number += 1

    win_label.config(text=who_win)


def new_game():
    want_play_again_label = Label(text="Do you want play again?", font=Font)
    want_play_again_label.grid(row=6, column=1, pady=20)

    want_play_again_button_1 = Button(text="Yes", font=Font, command=new_game_yes)
    want_play_again_button_1.grid(row=7, column=0)

    want_play_again_button_2 = Button(text="No", font=Font)
    want_play_again_button_2.grid(row=7, column=2)

def new_game_yes():
    global game_number
    global player_win

    games_number_label = Label(text=f"{player_win}/{game_number}", font=Font)
    games_number_label.grid(row=1, column=2)


my_window = Tk()
my_window.title("Rock, Paper, Scissors")
my_window.config(padx=50, bg="blue")

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

play_lab = Label(text="", font=Font)
play_lab.grid(column=0, row=4)

computer_label_thing = Label(text="", font=Font)
computer_label_thing.grid(row=4, column=2, pady=20)

win_label = Label(text="", font=Font)
win_label.grid(row=5, column=1)

canvas = Canvas(width=200, height=200, bg="blue", highlightthickness=0)
canvas_2 = Canvas(width=200, height=200, bg="blue", highlightthickness=0)
#picture file
scissor_img = PhotoImage(file="scissors.png")
rock_img = PhotoImage(file="rock.png")
paper_img = PhotoImage(file="paper.png")

#playeer image
player_image = canvas.create_image(100, 100)

#computer image
computer_image = canvas_2.create_image(100, 100)


canvas.grid(column=0, row=5)
canvas_2.grid(column=2, row=5)


my_window.mainloop()