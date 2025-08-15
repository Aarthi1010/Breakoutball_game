from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "magenta", "cyan"]

class Bricks:
    def __init__(self):
        self.bricks = []
        self.create_bricks()

    def create_bricks(self):
     for row in range(6):  # 6 rows of bricks
        y = 250 - row * 30
        for col in range(-550, 551, 110):  # columns from -550 to +550
            brick = Turtle()
            brick.shape("square")
            brick.shapesize(stretch_wid=1, stretch_len=5)
            brick.color(random.choice(COLORS))
            brick.penup()
            brick.goto(col, y)
            brick.quantity = 1
            self.bricks.append(brick)

