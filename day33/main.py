#1. Api

# import requests
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# lattitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, lattitude)
#
# print(iss_position)


#2. Kannye west project

# from tkinter import *
# import requests
#
#
# def get_quote():
#     response = requests.get(url="https://api.kanye.rest")
#     response.raise_for_status()
#     data = response.json()
#     canvas.itemconfig(quote_text, text=data['quote'])
#
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
#
# window.mainloop()

#3. Sunset, sunrise project

# import requests
# from datetime import datetime
#
# MY_LAT = 45.930459
# MY_LONG = 18.354493
#
# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LONG,
#     "formatted": 0
# }
#
# response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()
#
# sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
# sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
# print(sunrise)
# time_now = datetime.now()
#
# print(time_now)


#4. Iss and sunset

import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 45.930459
MY_LONG = 18.354493

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
my_email = "pista1125@gmail.com"
password = "tsewwfcqkvhforiy"

#Data from Iss_position


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data_iss = response.json()

    iss_longitude = float(data_iss["iss_position"]["longitude"])
    iss_lattitude = float(data_iss["iss_position"]["latitude"])

    if MY_LONG -5 <= iss_longitude <= MY_LONG +5 and MY_LAT -5 <= iss_lattitude <= MY_LAT +5:
        return True, iss_lattitude, iss_longitude
    else:
        return False


# Data from sun


def is_night():
    time_now = datetime.now().hour
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 2
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 2

    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False

#sending email


def send_email():
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=180) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="pista1125@gmail.com",
                            msg=f"Subject:Iss overhead\n\nLook up iss lattitude: {iss_overhead()[1]}, iss_longitude: {iss_overhead()[2]}")


while True:
    time.sleep(30)
    if iss_overhead() and is_night():
        send_email()