import random
import time
from turtle import Turtle, Screen
from player import Player
from car import Car
from scoreboard import ScoreBoard

screen = Screen()

screen.setup(600, 600)
screen.title("Turtle Racing Game")

x_co = 280

screen.tracer(0)
player = Player()
cars = Car()
scoreboard = ScoreBoard()
game_over = False
list_co = [-220, -180, -140, -100, -60, -20, 20, 60, 100, 140, 180, 220, ]
screen.listen()
screen.onkey(fun=player.move, key="w")
sleep_time = 0.1
while not game_over:
    time.sleep(sleep_time)
    cars.generate_car()
    cars.move()
    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_over = True

    if player.ycor() > 280:
        scoreboard.increase_level()
        sleep_time *= 0.9
        player.goto(0,-280)

    screen.update()
    if player.ycor() > 280:
        pass

screen.exitonclick()
