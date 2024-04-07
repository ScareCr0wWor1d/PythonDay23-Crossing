from turtle import Turtle
from random import randint

COLORS = ["pink", "orange", "yellow", "turquoise", "blue", "purple", "grey", "chocolate"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        randcolor = randint(0, 7)
        randy = randint(-250, 250)
        self.penup()
        self.shape("square")
        self.color(COLORS[randcolor])
        self.goto(300, randy)
        self.shapesize(stretch_wid=1, stretch_len=2)

    def move_auto(self):
        if self.xcor() > - 400:
            self.goto(self.xcor() - MOVE_INCREMENT, self.ycor())
