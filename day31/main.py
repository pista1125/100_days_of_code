import pandas
from tkinter import *
import random

current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("word_to_learn")
except:
    original_data = pandas.read_csv("eng-hun.csv", sep=";")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    my_windows.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_canvas, text="Angol", fill="black")
    canvas.itemconfig(word_canvas, text=current_card["Angol"], fill="black")
    canvas.itemconfig(background_canvas, image=photo_front)
    flip_timer = my_windows.after(3000, func=flip_card)

def remove():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("word_to_learn", index=False)

    next_card()


def flip_card():
    canvas.itemconfig(background_canvas, image=photo_back)
    canvas.itemconfig(title_canvas, text="Magyar")
    canvas.itemconfig(word_canvas, text=current_card["Magyar"])

my_windows = Tk()

my_windows.title("Flash card Project")
my_windows.config(bg="green", pady=50, padx=50)

flip_timer = my_windows.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800, highlightthickness=0, bg="green")

photo_front = PhotoImage(file="image/card_front.png")
photo_back = PhotoImage(file="image/card_back.png")

background_canvas = canvas.create_image(400, 263, image=photo_front)
title_canvas = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_canvas = canvas.create_text(400, 263, text="Word", font=("Ariel",60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#Button
ok_photo = PhotoImage(file="image/right.png")
wrong_photo = PhotoImage(file="image/wrong.png")

ok_button = Button(image=ok_photo, highlightthickness=0, command=remove)
wrong_button = Button(image=wrong_photo, highlightthickness=0, command=next_card)

ok_button.grid(column=0, row=1, padx=20)
wrong_button.grid(column=1, row=1, padx=20)
next_card()

my_windows.mainloop()