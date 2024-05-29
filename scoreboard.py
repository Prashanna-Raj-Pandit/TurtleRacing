from turtle import Turtle

FONT = ("Georgia", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1
        self.penup()
        self.goto(-280, 270)
        self.write_level(self.level)
        self.hideturtle()

    def write_level(self, level):
        self.write(f"Level :{level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write_level(self.level)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
