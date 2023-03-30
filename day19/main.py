#1. Turtle moodle with game
# import turtle
#
# timmy = turtle.Turtle()
# timmy.shape("turtle")
#
# def forward():
#     timmy.forward(10)
#
#
# def backward():
#     timmy.backward(10)
#
#
# def turn_left():
#     timmy.left(10)
#
#
# def turn_right():
#     timmy.right(10)
#
#
# def clear():
#     timmy.clear()
#     timmy.penup()
#     timmy.home()
#     timmy.pendown()
# timmy.penup()
# timmy.goto(-250, 0)
# timmy.pendown()
# my_srceen = turtle.Screen()
# my_srceen.listen()
# my_srceen.onkey(fun=forward, key="Up")
# my_srceen.onkey(fun=backward, key="Down")
# my_srceen.onkey(fun=turn_left, key="Left")
# my_srceen.onkey(fun=turn_right, key="Right")
# my_srceen.onkey(fun=clear, key="c")
# my_srceen.exitonclick()

#2. Turtle moodle with turtle race
# import turtle
# import random
#
# timmy_1 = turtle.Turtle()
# timmy_2 = turtle.Turtle()
# timmy_3 = turtle.Turtle()
# timmy_4 = turtle.Turtle()
# timmy_5 = turtle.Turtle()
#
# my_screen = turtle.Screen()
# my_screen.title("Welcome to the Turtle race!")
#
# guess = my_screen.textinput("which one will win?", "Let guess")
#
# timmy_1.shape("turtle"), timmy_1.penup(), timmy_1.setposition(-200, 0), timmy_1.color("red")
# timmy_2.shape("turtle"), timmy_2.penup(), timmy_2.setposition(-200, -100), timmy_2.color("blue")
# timmy_3.shape("turtle"), timmy_3.penup(), timmy_3.setposition(-200, -200), timmy_3.color("green")
# timmy_4.shape("turtle"), timmy_4.penup(), timmy_4.setposition(-200, 100), timmy_4.color("yellow")
# timmy_5.shape("turtle"), timmy_5.penup(), timmy_5.setposition(-200, 200), timmy_5.color("orange")
#
# game = True
#
# while game:
#     timmy_1.forward(random.randint(-2, 10))
#     timmy_2.forward(random.randint(-2, 10))
#     timmy_3.forward(random.randint(-2, 10))
#     timmy_4.forward(random.randint(-2, 10))
#     timmy_5.forward(random.randint(-2, 10))
#     x = timmy_1.pos()
#     y = timmy_2.pos()
#     z = timmy_3.pos()
#     l = timmy_4.pos()
#     p = timmy_2.pos()
#
#     if x >= (290.00, 0.00) or y >= (290.00, -100.00) or z >= (290.00, -200.00) or\
#             l >= (290.00, 100) or\
#             p >= (290.00, 200):
#         game = False
#
#
# my_screen.exitonclick()


#3. Turtle moodle with turtle race origin version
#
# from turtle import Turtle, Screen
# import random
#
# my_sreen = Screen()
# guess = my_sreen.textinput(title="Guess the winner", prompt="Who will win?")
#
# color = ["red", "blue", "green", "yellow", "orange"]
# y_position = [-200, -100, 0, 100, 200]
# all_turtle = []
#
# for timmy_index in range(0, 5):
#     timmy = Turtle(shape="turtle")
#     timmy.color(color[timmy_index])
#     timmy.penup()
#     timmy.goto(x=-200, y=y_position[timmy_index])
#     all_turtle.append(timmy)
#
# game_on = True
# while game_on:
#     for turtle in all_turtle:
#         if turtle.xcor() > 290:
#             game_on = False
#             winning = turtle.pencolor()
#             if winning == guess:
#                 print(f"You have won! The {winning} turtle is the winner!")
#             else:
#                 print(f"You have lost! The {winning} turtle is the winner!")
#         rand_distance = random.randint(-2, 10)
#         turtle.forward(rand_distance)
#
# my_sreen.exitonclick()

#4. flower with turtle

# from turtle import Turtle, Screen
#
# timmy = Turtle(shape="turtle")
# timmy.speed("normal")
# for x in range(6):
#     timmy.circle(100)
#     timmy.right(60)
# timmy.penup()
# timmy.forward(100)
# timmy.left(90)
# timmy.pendown()
# timmy.circle(100)

my_screen = Screen()
my_screen.exitonclick()
