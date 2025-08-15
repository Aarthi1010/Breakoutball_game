from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, lives=3):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-580, 260)
        self.score = 0
        self.lives = lives
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  Lives: {self.lives}", align="left", font=("Courier", 16, "normal"))

    def increase_score(self):
        self.score += 10
        self.update_scoreboard()

    def decrease_lives(self):
        self.lives -= 1
        self.update_scoreboard()

    def reset(self):
        self.score = 0
        self.lives = 5
        self.update_scoreboard()
