from turtle import Turtle
import random

MOVE_DIST = 8

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.speed_factor = 0.5 
        self.x_move_dist = random.choice([-MOVE_DIST, MOVE_DIST])
        self.y_move_dist = MOVE_DIST
        self.goto(0, -100)

    def move(self):
        new_x = self.xcor() + self.x_move_dist
        new_y = self.ycor() + self.y_move_dist
        self.goto(new_x, new_y)

    def bounce(self, x_bounce=False, y_bounce=False):
        if x_bounce:
            self.x_move_dist *= -1
        if y_bounce:
            self.y_move_dist *= -1

    def reset(self):
        self.goto(0, -240)
        self.x_move_dist = random.choice([-MOVE_DIST, MOVE_DIST])
        self.y_move_dist = MOVE_DIST

        
