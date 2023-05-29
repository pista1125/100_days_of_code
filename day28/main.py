from tkinter import *
import time

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

def start():
    timer.config(text="Work")
    for x in range(25, 0, -1):
                

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#tomato
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

#Label

timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW, highlightthickness=0)
timer.grid(row=0, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 12), command=start)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 12))
reset_button.grid(row=2, column=2)

check_label = Label(text="✔", bg=YELLOW, fg=GREEN, highlightthickness=0)
check_label.grid(row=3, column=1)
window.mainloop()