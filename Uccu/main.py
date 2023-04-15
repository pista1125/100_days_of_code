

word = ["cigány bűnözés", "vándorlás","Kanalazik", "Zsebtolvaj", "Üstfoltozó", "Zene", "Stétberger Ferenc",
        "cigány karaván", "jós", "gyűlölet bűncselekmény", "cigánykerék", "tenyérből jóslás", "letakarja a tükröt"
        "Vándorlás", "szőnyegkészítő", "teknővájó", "szekér", "macskajaj", "jósnő", "szoknya", "keresztelő", "lókupec",
        "fekete malac", "cirkusz", "roma szakkollégium", "szegregáció", "Virrasztás", "Romungró (magyarcigány)", "kéretés",
        "pipa", "identitás", "lecsó", "kalap", "cigány", "bazi nagy roma lagzi", "Szotyi", "LL junior", "Tánc",
        "rabszolgaság", "cigánybűnözés", "cigánykerék", "bodak (cigánykenyér)", "Punya (cigánykenyér)", "Kirekesztés",
        "diszkirimáció", "fux", "sátor", "Cigány himnusz", "Teknővájó", "Teknő", "Vajda", "száztagú cigányzenekar",
        "kosárfonó"]

word_1 = []
for x in word:
        y = x.title()
        word_1.append(y)

from turtle import Turtle, Screen
import random
choice_word = random.choice(word)

my_screen = Screen()
my_screen.bgpic("Flag_of_the_Romani_people.jpg")
my_screen.setup(width=500, height=400)
my_screen.listen()


def timmy_write():
        timmy.clear()
        choice_word = random.choice(word_1)
        timmy.write(f"A te szavad: {choice_word}", move=False, align="center", font=("Arial", 16, "normal"))

timmy = Turtle()
timmy.penup()
timmy.hideturtle()
timmy.color("gold")
timmy.goto(0, 75)
timmy.write(f"Nyomd meg a space billentyűt a szóválasztásért", move=False, align="center", font=("Arial", 16, "normal"))

my_screen.onkey(timmy_write, "space")


my_screen.mainloop()