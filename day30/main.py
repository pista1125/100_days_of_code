#1. Error type

#FileNotFound

# with open("a_file.txt") as file:
#     file.read()

#KeyError

# a_dictionary = {"key":"Value"}
# value = a_dictionary["non_exist_key"]

#IndexError

# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#TypeError

# text = "abc"
# print(text + 5)

#2. Solution to error: try, except, else, finally (raise)

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"Key": "Value"}
#     print(a_dictionary["Key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key: {error_message} does not exist")
# else:
#     print("hello")
# finally:
#     file.close()
#     print("File was closed")
#     raise TypeError("This is an error that I made up")

#3. example to raise function:

# height = float(input("What is your height: "))
# weight = float(input("What is your weight: "))
#
# if height > 3:
#     raise ValueError("The height is too much")
# bmi = weight / height ** 2
#
# print(bmi)

#4. Coding excersise 1.

# fruits = ["Apple", "Pear", "Orange"]
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
# make_pie(4)

#5. exercise coding 2.
# facebook = {"comment": 20, "share": 1}
#
# facebook["like"] = 20
# print(facebook)
#
#
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
# total_likes = 0
#
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except:
#         post['Likes'] = 0
#         total_likes = total_likes + post["Likes"]
#
# print(total_likes)


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


#6. Nato phonetic problem
# import pandas
#
# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)
#
# def alphabet():
#     word = input("Enter a word: ").upper()
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please")
#         alphabet()
#     else:
#         print(output_list)
#
# alphabet()

#7. Password manager turbo edition

from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

def password_generate():
    #Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    password_entry.insert(0, password)

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) ==0:
        messagebox.showinfo(title="Opps", message="You missed one")
    else:
        #in the project
        try:
            with open(file="data.json", mode="r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open(file="data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exist.")

my_window = Tk()
my_window.title("Password Manager")
my_window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

#Label

website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

#Entry
website_entry = Entry(width=20)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.insert(0, "orsos.istvan@pte.hu")
password_entry = Entry(width=18)

website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
password_entry.grid(row=3, column=1, sticky="w")

#Button

add_button = Button(text="Add", width=34, command=save)
generate_button = Button(text="Generate Password", command=password_generate)
search_button = Button(text="Search", width=12, command=search)

add_button.grid(row=4, column=1, columnspan=2, sticky="w")
generate_button.grid(row=3, column=1, sticky="e")
search_button.grid(row=1, column=1, sticky="e")

my_window.mainloop()

#8. Work with json file

# write json file: mode= "w"
#with open(file="data.json", mode="w") as data_file:
    #json.dump(new_data, data_file, indent=4)

# Load json file: mode="r"
#with open(file="data.json", mode="r") as data_file:
    #data = json.load(data_file)

# Update json file:
# with open(file="data.json", mode="r") as data_file:
#     #Reading old data
#     data = json.load(data_file)
#     #updating old data with new data
#     data.update(new_data)
# with open("data.json", "w") as data_file:
#     #Saving updated data
#     json.dump(data, data_file, indent=4)

