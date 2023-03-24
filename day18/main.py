#1. timmy geometry
# from turtle import Turtle, Screen
# import random
# timmy = Turtle()
# timmy.shape("turtle")
#
# list = ["red", "blue", "silver", "medium slate blue"]
#
# for x in range(8):
#     color = random.choice(list)
#     timmy.color(color)
#     a = int(360 / (x+3))
#     for y in range(int(360 / a)):
#         timmy.right(a)
#         timmy.forward(50)
#
# my_screen = Screen()
# my_screen.exitonclick()
# import turtle
# from random import *
#
# print(choice([1,2,3]))

#2. timmy geometry
# from turtle import Turtle, Screen
# import random
# timmy = Turtle()
# timmy.shape("turtle")
# list = ["red", "blue", "silver", "medium slate blue"]
#
# def draw(number):
#     angle = 360 / number
#     for _ in range(number):
#         timmy.right(angle)
#         timmy.forward(50)
#
# for side in range(3, 11):
#     color = random.choice(list)
#     timmy.color(color)
#     draw(side)
#
# my_screen = Screen()
# my_screen.exitonclick()

#3. timmy random walk, with random color
# import turtle
# from turtle import Turtle, Screen
# import random
# timmy = Turtle()
# timmy.shape("turtle")
#
# turtle.colormode(255)
# timmy.speed("fastest")
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b
#
#
# for _ in range(200):
#     timmy.pensize(10)
#     number = random.choice([0, 90, 180, 270])
#     timmy.pencolor(random_color())
#     timmy.forward(20)
#     timmy.setheading(number)
#
#
# my_screen = Screen()
# my_screen.exitonclick()

#3. timmy random walk, with random color
# import turtle
# from turtle import Turtle, Screen
# import random
#
# timmy = Turtle()
# timmy.shape("turtle")
# turtle.colormode(255)
# timmy.speed("fastest")
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b
#
#
# def draw_circle(number):
#     for _ in range(int(360 / number)):
#         timmy.pencolor(random_color())
#         timmy.circle(100)
#         timmy.right(number)
#
#
# draw_circle(60)
# timmy.penup()
# timmy.forward(100)
# timmy.pendown()
# timmy.left(90)
# timmy.circle(100)
#
#
#
# my_screen = Screen()
# my_screen.exitonclick()

#4. hirst spot painting

# import colorgram
# rgb_colors = []
# color = colorgram.extract('picture.jpg', 30)
#
# for item in color:
#     r = item.rgb.r
#     g = item.rgb.g
#     b = item.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
#
# color_list = [(246, 242, 234), (248, 241, 245), (239, 247, 242), (239, 242, 247), (197, 165, 117), (142, 80, 56), (220, 201, 137), (59, 94, 119), (164, 152, 53), (136, 162, 181), (131, 34, 22), (69, 39, 32), (53, 117, 86), (192, 95, 78), (146, 177, 149), (19, 91, 68), (165, 143, 157), (31, 59, 76), (111, 75, 81), (228, 176, 164), (128, 29, 33), (179, 204, 177), (71, 34, 36), (25, 82, 89), (89, 146, 127), (18, 69, 57), (41, 66, 90), (219, 178, 182), (175, 94, 98), (179, 192, 205)]


#5. timmy hirst spot painting

import turtle
import random

color_list = [(246, 242, 234), (248, 241, 245), (239, 247, 242), (239, 242, 247), (197, 165, 117), (142, 80, 56), (220, 201, 137), (59, 94, 119), (164, 152, 53), (136, 162, 181), (131, 34, 22), (69, 39, 32), (53, 117, 86), (192, 95, 78), (146, 177, 149), (19, 91, 68), (165, 143, 157), (31, 59, 76), (111, 75, 81), (228, 176, 164), (128, 29, 33), (179, 204, 177), (71, 34, 36), (25, 82, 89), (89, 146, 127), (18, 69, 57), (41, 66, 90), (219, 178, 182), (175, 94, 98), (179, 192, 205)]

timmy = turtle.Turtle()
turtle.colormode(255)

timmy.penup()
timmy.hideturtle()
timmy.speed("fastest")
timmy.setheading(225)
timmy.forward(330)
timmy.setheading(0)

number_dot = 100

for n in range(1, number_dot + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)
    if n % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

my_screen = turtle.Screen()
my_screen.exitonclick()