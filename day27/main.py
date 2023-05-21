#1. TK inter begining
# import tkinter
#
# window = tkinter.Tk()
# window.title("My first GUI program")
# window.minsize(width=500, height=300)
#
#
# my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
#
#
#
# window.mainloop()

#2. default values

# def my_function(a=1, b=2):
#     print(a,b)
#
# my_function()

#3. unlimited argument

# def my_funciton(*args):
#     #print(args[1])
#     add = 0
#     for n in args:
#         add += n
#     print(add)
# my_funciton(1,2,3,4)

#4. keyword arguments

# def calculate(n, **kwargs):
#     print(n)
#     # for key, argue in kwargs.items():
#     #     print(key)
#     #     print(argue)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
# calculate(5, add=3, multiply=5)

#5. keyworg with class

# class Car:
#     def __init__(self, **kw):
#         #self.make = kw["makes"]
#         #self.model = kw["models"]
#
#         #You will not give an error
#         self.make = kw.get("makes")
#         self.model = kw.get("models")
#
# my_car = Car(models="G Astra")
#
# print(my_car.model)

#6. TK inter continue

# from tkinter import *
#
# window = Tk()
# window.title("My first GUI program")
# window.minsize(width=500, height=300)
#
#
# my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
#
# #configure the label parameters
# # my_label["text"] = "new text"
# # my_label.config(text="New text")
# def button_clicked():
#     new_text = input.get()
#     my_label.config(text=new_text)
# my_button = Button(text="Click me", command=button_clicked)
# my_button.pack()
#
# #Entry
#
# input = Entry(width=10)
# input.pack()
#
#
# window.mainloop()


#7. some widget from tkinter

# from tkinter import *
#
# #Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)
#
# #Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()
#
# #Buttons
# def action():
#     print("Do something")
#
# #calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()
#
# #Entries
# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# #Gets text in entry
# print(entry.get())
# entry.pack()
#
# #Text
# text = Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()


#8. TK inter continue

# from tkinter import *
#
# window = Tk()
# window.title("My first GUI program")
# window.minsize(width=500, height=300)
# window.config(padx=20, pady=20)
#
#
# my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# #I have 3 option: pack, place, grid
# #my_label.place(width=300, height=200)
# my_label.grid(row=0, column=0)
#
# #configure the label parameters
# # my_label["text"] = "new text"
# # my_label.config(text="New text")
#
# #Button
#
# def button_clicked():
#     new_text = input.get()
#     my_label.config(text=new_text)
# my_button = Button(text="Click me", command=button_clicked)
# my_button.grid(row=1, column=1)
#
# new_button = Button(text="new button")
# new_button.grid(column=2, row=0)
#
# #Entry
#
# input = Entry(width=10)
# input.grid(row=2, column=3)
#
#
# window.mainloop()

#9. Mile to km tkinter

from tkinter import *

my_window = Tk()
my_window.title("Mile to Km converter")
my_window.config(padx=20, pady=20)

#Button

def calculate():
    number_mile = float(entry.get())
    number_km = round(number_mile * 1.6, 2)
    my_label_3.config(text=f"{number_km}")

my_button = Button(text="Calculate", command=calculate)
my_button.grid(row=2, column=1)

#Entry

entry = Entry(width=10)
entry.grid(row=0, column=1)

#Label
my_label = Label(text="is equal to")
my_label.grid(row=1, column=0)

my_label_2 = Label(text="Mile")
my_label_2.grid(row=0, column=2)

my_label_3 = Label(text="0")
my_label_3.grid(row=1, column=1)

my_label_4 = Label(text="Km")
my_label_4.grid(row=1, column=2)

my_window.mainloop()