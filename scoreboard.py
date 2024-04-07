from turtle import Turtle

FONT = ("Courier", 24, "normal")
FONTGO = ("consolas", 36, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('blue')
        self.hideturtle()
        self.penup()
        self.goto(-200, 260)
        self.updatesb(1)

    def updatesb(self, niv):
        self.clear()
        self.write(f"Level: {niv}", font=FONT, align='center')

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.color('red')
        self.write("GAME OVER", font=FONTGO, align='center')
