#1. Email sending with python
# import smtplib
#
# my_email = "pista1125@gmail.com"
# password = "tsewwfcqkvhforiy"
# #encoding: "iso-8859-1" if outlook, utf-8 if gmail
#
# with smtplib.SMTP("smtp.gmail.com", 587, timeout=180) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="orsos.istvan@pte.hu",
#                         msg="Subject:Hello\n\nEzt a pythonbol küldöm most neked!".encode("utf-8"))
import random

#2. datatime module
# import datetime as dt
#
# now = dt.datetime.now()
# print(now)
# year = now.year
# month = now.month
# day_of_week = now.weekday()
#
# date_of_birth = dt.datetime(year=1995, month=11, day=25)
# print(date_of_birth)


#3. Sending email with motivation letter

# import smtplib
# import random
# import datetime as dt
#
# my_email = "pista1125@gmail.com"
# password = "tsewwfcqkvhforiy"
# to_address = "orsos.istvan@pte.hu"
#
# now = dt.datetime.now()
# weekday = now.weekday()
#
# if weekday == 2:
#     with open("quotes.txt") as file:
#         file_list = file.readlines()
#         letter = random.choice(file_list)
#
#     with smtplib.SMTP("smtp.gmail.com", 587, timeout=180) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email, to_addrs=to_address,
#                             msg=f"Subject:Motivation\n\n{letter}")


#4. Automated birthday wisher

import pandas
import smtplib
import datetime as dt
import random

#read birthday file, and all letter.

birthday = pandas.read_csv("birthdays.csv")
birthday_dict = birthday.to_dict(orient="records")

with open("letter/letter_1.txt") as letter_1_file:
    letter_1 = letter_1_file.read()
with open("letter/letter_2.txt") as letter_2_file:
    letter_2 = letter_2_file.read()
with open("letter/letter_3.txt") as letter_3_file:
    letter_3 = letter_3_file.read()

letters = [letter_1, letter_2, letter_3]

#What is today
now = dt.datetime.now()
month = now.month
day = now.day


my_email = "pista1125@gmail.com"
password = "tsewwfcqkvhforiy"

to_address = None
name = None

#searching people who has a birthday today:
for x in birthday_dict:
    if x["month"] == month and x["day"] == day:
        to_address = x["email"]
        name = x["name"]

        #chooce a letter, and replace name to it
        letter = random.choice(letters)
        letter = letter.replace("[NAME]", name)

        #finally sending an email
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=180) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=to_address,
                                    msg=f"Subject:Happy Birthday\n\n{letter}"
                            )