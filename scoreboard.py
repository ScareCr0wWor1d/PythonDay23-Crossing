import time
from turtle import Turtle

FONT = ("Courier", 24, "normal")
FONTGO = ("consolas", 36, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('blue')
        self.hideturtle()
        self.updatesb(1)

    def updatesb(self, niv):
        self.penup()
        self.goto(-200, 260)
        self.clear()
        self.write(f"Level: {niv}", font=FONT, align='center')
        self.drawboard()

    def game_over(self):
        self.penup()
        self.clear()
        self.goto(0, 0)
        self.color('red')
        self.write("GAME OVER", font=FONTGO, align='center')

    def drawboard(self):
        self.goto(-300, -260)
        self.color('white')
        self.pendown()
        self.goto(300, -260)
        self.penup()
        self.goto(-300, 260)
        self.pendown()
        self.color('white')
        self.pendown()
        self.goto(300, 260)