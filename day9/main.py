#1. Dictionary functions

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }
#
# # print(programming_dictionary["Bug"])
# #add a new key
# programming_dictionary["Loop"] = "The action of doing something over and over again."
#
# # print(programming_dictionary)
# #Edit an item in dictionary
#
# programming_dictionary["Bug"] = "A moth in your computer"
# # print(programming_dictionary)
#
# #Loop in dictionary
#
# for thing in programming_dictionary:
#     print(thing)
#     print(programming_dictionary[thing])

#2. Grading program

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# student_grades = {}
#
# for student in student_scores:
#     if student_scores[student] > 90:
#         student_grades[student] = "Outstanding"
#     elif student_scores[student] > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif student_scores[student] > 70:
#         student_grades[student] = "Acceptable"
#     elif student_scores[student] <= 70:
#         student_grades[student] = "Fail"
#
# print(student_grades)

#3. Nesting (distionary, and list)

# travel_log = {
#     "France": {"cities_visited":["Parizs", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "hamburg", "Stuttgart"], "total_visits": 5},
# }
#
# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Parizs", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "hamburg", "Stuttgart"],
#         "total_visits": 5
#     },
# ]

#4. Dictionary in list my version

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# travel_log.append({"country": "Russia", "visits": 2, "cities": ["Moscow", "Saint Petersburg"]})

#add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

#4. Dictionary in list my version

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]

# def add_new_country(country_visited, times_visited, citi_visited):
#     new_country = {}
#     new_country["country"] = country_visited
#     new_country["visits"] = times_visited
#     new_country["cities"] = citi_visited
#     travel_log.append(new_country)
#
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


# important code from quiz
# print(travel_log[0]["cities"][2])

#6. Final game

game = []
def person(name, score):
    extend = {}
    extend["name"] = name
    extend["score"] = score
    game.append(extend)

eper_final = []
def calculator(eper_final):
    eper = []
    for score in game:
        a = score["score"]
        eper.append(a)
    eper_final += eper
    b = (max(eper_final))
    position = eper_final.index(b)
    print(f"Winner is {game[position]['name']} because she/he score was {game[position]['score']}.")
game_end = True
while game_end:
    n = input("what is your name?\n")
    s = int(input("What is your score?\n"))
    person(n, s)
    h = input("do you want continue? type yes, or no\n")
    if h == 'no':
        game_end = False
    elif h == "yes":
        game_end = True
    else:
        game_end = False
        print("You are stupid")

calculator(eper_final)
