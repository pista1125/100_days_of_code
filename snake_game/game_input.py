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
        self.bounce = ["Bounce wall", "not bounce wall"]
        self.bounce_wall = 0
        self.timmy_wall = []


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
        elif self.menu == 1:
            for timmy in self.timmy_speed:
                timmy.clear()
            self.menu += 1
        elif self.menu == 2:
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
        elif y < -20:
            self.bounce_wall = 2

