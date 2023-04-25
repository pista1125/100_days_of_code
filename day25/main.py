#1. open a csv file
# with open("weather_data.csv") as data:
#     weather = data.readlines()
#     print(weather)

#2. open a csv file and take separate list using csv library.
# import csv
# with open("weather_data.csv") as data:
#     weather = csv.reader(data)
#     temperatures = []
#     for row in weather:
#         if row[1] != "temp":
#             temp = int(row[1])
#             temperatures.append(temp)
#     print(temperatures)

#3. open a csv file with pandas.

import pandas

# data = pandas.read_csv("weather_data.csv")

# print(type(data))
# data_dic = data.to_dict()
# print(data_dic)
#
# temp_list = data["temp"].to_list()
# print(type(data["temp"]))
# print(temp_list)

#1. avarage one way
# avarage = sum(temp_list) / len(temp_list)
# print(avarage)

#2. avarage other way
# avarage = data["temp"].mean()
# print(avarage)

# print(data["temp"].max())

#Get a Data in coloums
# print(data["condition"])
# print(data.condition)

#get data in row

# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

#Create a dataFrame from scratch

# data_dict = {
#     "student": ["Any", "James", "Istvan"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

#3. squirrel project

# import pandas
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
# gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
# print(red_squirrel_count)
# print(black_squirrel_count)
# print(gray_squirrel_count)
#
# data_dict = {
#     "Fur color": ["Gray", "Black", "Cinnamon"],
#     "Count": [gray_squirrel_count, black_squirrel_count, red_squirrel_count]
# }
#
# df = pandas.DataFrame(data_dict)
#
# df.to_csv("squirrel_count.csv")

#4. US State project

import turtle

my_screen = turtle.Screen()
my_screen.title("USA")
my_screen.bgpic("blank_states_img.gif")





my_screen.exitonclick()
