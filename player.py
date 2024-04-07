import time
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('green')
        self.left(90)
        self.shape('turtle')
        self.goto(STARTING_POSITION)

    def move_f(self):
        self.goto(self.xcor(), self.ycor()+MOVE_DISTANCE)

    def pos_init(self):
        self.goto(STARTING_POSITION)

    def ecrapou(self, screen):
        self.shape('circle')
        self.color('red')
        for i in range(1, 4):
            self.shapesize(i)
            time.sleep(0.08)
            screen.update()
