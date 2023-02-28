
# print("1233"[2])
# "helo"[3]
# print(1.2+3)

'''
num_char = (len(input("what")))
new_num_char = str(num_char)
print("your " + new_num_char + " character")
'''
'''
weight = input("What is your weight? (kg) ")
height = input("what is your hight? (m) ")
#BMI calculator
a = float(weight)
b = float(height)
c = round( a / (b * b), 2 )

print(f"Your BMI is {c}")
'''
'''
score = 3

score /=1
print(score)
'''

'''
#How many time do you have yet!
age = input("What is your current age? ")

days = (90 - int(age)) * 365
weeks = (90 - int(age)) * 52
months = (90 - int(age)) * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
'''

#Tip calculator

print("Welcome to the tip calculator!")
total = float(input("What was the total bill? "))
tip = float(input("How much tip would you like to give? 10, 12, 15? "))
people = float(input("How many people to split the bill? "))


result = (total * (1 + tip / 100)) / people
result_1 = "{:.2f}".format(result)
print(f"Each person should be pay: {result_1}")





