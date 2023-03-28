from turtle import Turtle

art = '''               
                
                
                UP
               
LEFT    DOWN   RIGHT'''

class GameStart(Turtle):
    def __init__(self):
        super().__init__()
        self.time = 3
        self.color("white")
        self.hideturtle()
        self.penup()
        self.button = art
    def Start(self):
        self.write(f"Game will be start at: {self.time}\n {self.button} ", False, "center", ("Arial", 12, "normal"))
        self.time -= 1


