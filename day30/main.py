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

facebook = {"comment": 20, "share": 1}

facebook["like"] = 20
print(facebook)


facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except:
        post['Likes'] = 0
        total_likes = total_likes + post["Likes"]


print(total_likes)



# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
