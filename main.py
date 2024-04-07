import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

speed = 0.2

compteur = 0
level = 1
totue = Player()
parking_lot = []
char = CarManager()
parking_lot.append(char)
niv = Scoreboard()
screen.onkeypress(totue.move_f, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(speed)
    if compteur == 5:
        char = CarManager()
        parking_lot.append(char)
        compteur = 0
    for char in parking_lot:
        char.move_auto()
        if totue.distance(char) < 30:
            game_is_on = False
            totue.ecrapou(screen)
    compteur += 1
    screen.update()
    if totue.ycor() == 280:
        totue.pos_init()
        level += 1
        speed *= 0.7
        niv.updatesb(level)

niv.game_over()
screen.exitonclick()
