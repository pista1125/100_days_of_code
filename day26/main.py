#1. List comprehension with list

# number = [1, 2, 3]
# add_number = [n + 1 for n in number]
# print(add_number)

#2. List comprehension with string

# name = "Istvan"
# new_list = [n for n in name]
# print(new_list)

#3. List comprehension with range function
# number = range(1, 5)
#
# list = [n * 2 for n in range(1, 5)]
# print(list)

#4. List comprehension with if function

# name = ["Istvan", "Jozsi", "Barbara", "Bernadett", "Eper"]
# short_name = [n.upper() for n in name if len(n) < 6]
# print(short_name)

#5. Coding exercise.

#1. exercise

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n**2 for n in numbers]
# print(squared_numbers)

#2. exercise

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [n for n in numbers if n % 2 == 0]
# print(result)

#3. exercise

# with open("file1.txt") as file_1:
#     data_1 = file_1.readlines()
#
# with open("file2.txt") as file_2:
#     data_2 = file_2.readlines()
#
# result = [int(n) for n in data_1 if n in data_2]
#
#
# print(result)


#6. US State project turbo wersion

# import turtle
# import pandas
# my_screen = turtle.Screen()
# my_screen.title("USA")
# image = "blank_states_img.gif"
# my_screen.addshape(image)
# turtle.shape(image)
#
# data = pandas.read_csv("50_states.csv")
# all_states = data.state.to_list()
# guessed_states = []
#
# while len(guessed_states) < 50:
#     answer_state_1 = my_screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Whats the another state's name?")
#     answer_state = answer_state_1.title()
#     if answer_state == "Exit":
#         missing_states = [n for n in all_states if n not in guessed_states]
#         new_data = pandas.DataFrame(missing_states)
#         new_data.to_csv("states_to_learn.csv")
#         break
#     if answer_state in all_states:
#         guessed_states.append(answer_state)
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_data = data[data.state == answer_state]
#         t.goto(int(state_data.x), int(state_data.y))
#         t.write(answer_state)

#7. Dictionary comprehension loop for list
# import random
#
# name = ["Istvan", "Jozsi", "Barbara", "Bernadett", "Eper"]
#
# student_score = {n: random.randint(1, 100) for n in name}
# print(student_score)

#8. Dictionary comprehension use dictionary

# student = {'Istvan': 68, 'Jozsi': 13, 'Barbara': 79, 'Bernadett': 34, 'Eper': 18}
#
# pass_student = {x: y for (x, y) in student.items() if y > 60}
#
# print(pass_student)

#9. Coding exercise with dictionary comprehension

#1. exercise

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# sentence_list = sentence.split()
#
# result = {x: len(x) for x in sentence_list}
#
# print(result)

#2. exercise

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {x: (y * 9/5) + 32 for (x, y) in weather_c.items()}
#
# print(weather_f)

#10. iterate over pandas DataFrame

student_dict = {
    "student": ["Istvan", "James", "Angela"],
    "score": [98, 76, 54]
}
#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

# import pandas
#
# student_data_frame = pandas.DataFrame(student_dict)

# print(student_data_frame)

#Loop throught a data frame

# for (key, value) in student_data_frame.items():
#     print(value)

#Loop through rows of a data frame

# for (index, row) in student_data_frame.iterrows():
#     # print(row.student) # or score
#     if row.student == "Istvan":
#         print(row.score)

#11. NATO alphabet

import pandas

data_dict = {row.letter: row.code for (index, row) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}

user_name = input("What is your name?: ").upper()

solution = [data_dict[n] for n in user_name]
print(solution)