from turtle import Turtle

class Game_input:
    def __init__(self):
        self.menu = 0
        #This code is about a player count
        self.player_number = 0
        self.x_position = [30, -30]
        self.y_position = -100
        self.timmy_player =[]
        #This code is about a player speed
        self.speed = 0
        self.timmy_speed = []
        self.x_speed_position = [30, 0, -30]
        self.y_speed_position = -100
        self.choice_dif_level = ["hard", "normal", "easy"]
        #This code about a bounce wall
        self.bounce = ["Not bounce wall", "Bounce wall"]
        self.bounce_wall = 0
        self.timmy_wall = []
        #this code about a snake color setting
        self.x_color_position = [-100, -50, 0, 50, 100, 150]
        self.y_color_position = 30
        self.color_option = ["white", "red", "blue", "green", "yellow", "orange"]
        self.timmy_color = []
        self.color_choice = "blue"
        self.color = 0

    def player(self):
        for x in range(2):
            timmy = Turtle()
            timmy.color("white")
            timmy.hideturtle()
            timmy.penup()
            timmy.goto(self.y_position, self.x_position[x])
            timmy.write(f"{x+1} Player", False, "center", ("Arial", 12, "normal"))
            self.timmy_player.append(timmy)

    def choice_number(self, x, y):
        if y > 20:
            self.player_number = 1
        elif y < -20:
            self.player_number = 2

    def speed_turtle(self):
        for x in range(3):
            timmy = Turtle()
            timmy.color("white")
            timmy.hideturtle()
            timmy.penup()
            timmy.goto(self.y_speed_position, self.x_speed_position[x])
            timmy.write(f"{self.choice_dif_level[x]} Player", False, "center", ("Arial", 12, "normal"))
            self.timmy_speed.append(timmy)

    def choice_speed(self, x, y):
        if y > 25:
            self.speed = 0.05
        elif 25 > y > -25:
            self.speed = 0.1
        elif y < -25:
            self.speed = 0.2

    def all_timmy_clear(self):
        if self.menu == 0:
            for timmy in self.timmy_player:
                timmy.clear()
            self.menu += 1
        # elif self.menu == 1:
        #     for timmy in self.timmy_color:
        #         timmy.clear()
        #     self.menu += 1
        elif self.menu == 1:
            for timmy in self.timmy_speed:
                timmy.clear()
            self.menu += 2
        elif self.menu == 3:
            for timmy in self.timmy_wall:
                timmy.clear()


    def wall_turtle(self):
        for x in range(2):
            timmy = Turtle()
            timmy.color("white")
            timmy.hideturtle()
            timmy.penup()
            timmy.goto(self.y_position, self.x_position[x])
            timmy.write(f"{self.bounce[x]} ", False, "center", ("Arial", 12, "normal"))
            self.timmy_wall.append(timmy)

    def choice_bounce(self, x, y):
        if y > 20:
            self.bounce_wall = 1
        elif y < -10:
            self.bounce_wall = 2

    # def color_setting(self):
    #     for x in range(6):
    #         timmy = Turtle()
    #         timmy.color("white")
    #         timmy.hideturtle()
    #         timmy.penup()
    #         timmy.goto(self.x_color_position[x], self.y_color_position)
    #         timmy.write(f"{self.color_option[x]}", False, "center", ("Arial", 12, "normal"))
    #         self.timmy_color.append(timmy)

    # def choice_color(self, x, y):
    #     if y > 20 and -125 < x < -75:
    #         self.color_choice = "red"
    #         print(self.color_choice)
    #         self.color = 1
    #     elif y > 20 and -75 < x < -25:
    #         self.color_choice = "blue"
    #         self.color = 1
    #     elif y > 20 and -25 < x < 25:
    #         self.color_choice = self.color_option[2]
    #         self.color = 1
    #     elif y > 20 and 25 < x < 75:
    #         self.color_choice = self.color_option[3]
    #         self.color = 1
    #     elif y > 20 and 75 < x < 125:
    #         self.color_choice = self.color_option[4]
    #         self.color = 1
    #     elif y > 20 and 125 < x < 175:
    #         self.color_choice = self.color_option[5]
    #         self.color = 1

