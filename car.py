import random
from turtle import Turtle

colors = ["forest green", "firebrick", "dark orchid", "gold", "light slate gray", "magenta", "black"]


class Car:
    def __init__(self):
        self.all_cars = []

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(colors))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(5)
