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

name = ["Istvan", "Jozsi", "Barbara", "Bernadett", "Eper"]
short_name = [n.upper() for n in name if len(n) < 6]
print(short_name)