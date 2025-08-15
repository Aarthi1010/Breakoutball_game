import turtle as tr
import pygame
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from ui import UI
from bricks import Bricks

# Initialize pygame mixer
pygame.mixer.init()

# Setup screen
screen = tr.Screen()
screen.setup(width=1200, height=800)
screen.bgcolor('black')
screen.title('Breakout Game')
screen.tracer(0)

# Globals
game_paused = False
playing_game = True
restart_btn = tr.Turtle()
restart_btn.hideturtle()
restart_btn.penup()
restart_btn.speed(0)

# Game components
ui = UI()
score = Scoreboard(lives=5)
paddle = Paddle()
bricks = Bricks()
ball = Ball()

# Pause toggle
def pause_game():
    global game_paused
    game_paused = not game_paused

# Keyboard controls
screen.listen()
screen.onkey(paddle.move_left, 'Left')
screen.onkey(paddle.move_right, 'Right')
screen.onkey(pause_game, 'space')

# Collision checks
def check_collision_with_walls():
    global playing_game
    if ball.xcor() < -580 or ball.xcor() > 570:
        pygame.mixer.Sound("bounce.wav").play()
        ball.bounce(x_bounce=True, y_bounce=False)
    if ball.ycor() > 370:
        pygame.mixer.Sound("bounce.wav").play()
        ball.bounce(x_bounce=False, y_bounce=True)
    if ball.ycor() < -380:
        ball.reset()
        score.decrease_lives()
        if score.lives == 0:
            playing_game = False
            ui.game_over(False)
            show_restart_button()
        else:
            ui.change_color()


def check_collision_with_paddle():
    if ball.distance(paddle) < 60 and -270 < ball.ycor() < -230:
        pygame.mixer.Sound("bounce.wav").play()
        offset = ball.xcor() - paddle.xcor()
        ball.x_move_dist = offset * 0.4
        ball.bounce(y_bounce=True)



def check_collision_with_bricks():
    for brick in bricks.bricks[:]:
        if ball.distance(brick) < 40:
            pygame.mixer.Sound("bounce.wav").play()
            score.increase_score()
            brick.quantity -= 1
            if brick.quantity == 0:
                brick.clear()
                brick.goto(3000, 3000)
                bricks.bricks.remove(brick)
            ball_x, ball_y = ball.xcor(), ball.ycor()
            brick_x, brick_y = brick.xcor(), brick.ycor()

            if abs(ball_y - brick_y) > abs(ball_x - brick_x):
                ball.bounce(x_bounce=False, y_bounce=True)  # vertical hit (top/bottom)
            else:
                ball.bounce(x_bounce=True, y_bounce=False)  # horizontal hit (left/right)


# Draw restart button
def show_restart_button():
    restart_btn.clear()
    restart_btn.penup()
    restart_btn.goto(-75, -60)
    restart_btn.color("white", "green")
    restart_btn.begin_fill()
    for _ in range(2):
        restart_btn.forward(150)
        restart_btn.left(90)
        restart_btn.forward(40)
        restart_btn.left(90)
    restart_btn.end_fill()

    # Button text
    restart_btn.goto(0, -45)
    restart_btn.color("black")
    restart_btn.write("Restart", align="center", font=("Arial", 16, "bold"))

    screen.onclick(on_restart_click)

# Restart on button click
def on_restart_click(x, y):
    if -75 < x < 75 and -60 < y < -20:
        screen.onclick(None)
        restart_btn.clear()
        restart_game()

# Restart logic
def restart_game():
    global game_paused, playing_game

    paddle.goto(0, -250)
    ball.reset()
    score.reset()
    ui.header()

    for brick in bricks.bricks:
        brick.clear()
        brick.goto(3000, 3000)
    bricks.bricks.clear()
    bricks.create_bricks()

    game_paused = False
    playing_game = True

# Main persistent loop (never stops)
def run_forever_loop():
    global playing_game

    if playing_game:
        if not game_paused:
            screen.update()
            ball.move()

            check_collision_with_walls()
            check_collision_with_paddle()
            check_collision_with_bricks()

            if len(bricks.bricks) == 0:
                playing_game = False
                ui.game_over(True)
                show_restart_button()
        else:
            ui.paused_status()

    screen.ontimer(run_forever_loop,15)

# Start game
ui.header()
run_forever_loop()

# Keep window open
tr.mainloop()

