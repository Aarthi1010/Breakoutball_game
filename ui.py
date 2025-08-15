from turtle import Turtle

class UI(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()

    def header(self):
        self.clear()
        self.goto(0, 260)
        self.write("Breakout Game", align="center", font=("Courier", 24, "bold"))

    def game_over(self, won):
        self.goto(0, 0)
        msg = "You Win! 🎉" if won else "Game Over 😢"
        self.write(msg, align="center", font=("Courier", 30, "bold"))

    def paused_status(self):
        self.goto(0, -20)
        self.write("Game Paused. Press SPACE to Resume", align="center", font=("Courier", 16, "normal"))

    def change_color(self):
        colors = ["red", "blue", "green", "yellow", "white"]
        self.color(colors[self.xcor() % len(colors)])
