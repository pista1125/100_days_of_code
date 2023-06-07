from tkinter import *

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
website_entry = Entry(width=40)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.insert(0, "orsos.istvan@pte.hu")
password_entry = Entry(width=18)


website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
password_entry.grid(row=3, column=1, sticky="w")

#Button

add_button = Button(text="Add", width=34)
generate_button = Button(text="Generate Password")

add_button.grid(row=4, column=1, columnspan=2, sticky="w")
generate_button.grid(row=3, column=1, sticky="e")


my_window.mainloop()