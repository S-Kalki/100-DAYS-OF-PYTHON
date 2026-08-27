from turtle import Screen

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time


screen = Screen()

screen.setup(
    width=800,
    height=600
)

screen.bgcolor("black")
screen.title("My Pong Game")

screen.tracer(0)


# Create objects

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

ball = Ball()

scoreboard = Scoreboard()


# Keyboard controls

screen.listen()

# Left player
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

# Right player
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")


game_running = True


while game_running:

    screen.update()

    time.sleep(0.03)

    ball.move()


    # -------------------------
    # Wall collision
    # -------------------------

    if ball.ycor() > 280 or ball.ycor() < -280:

        ball.bounce_y()


    # -------------------------
    # Right paddle collision
    # -------------------------

    if (
        ball.xcor() > 320
        and ball.xcor() < 350
        and abs(ball.ycor() - right_paddle.ycor()) < 50
    ):

        ball.bounce_x()


    # -------------------------
    # Left paddle collision
    # -------------------------

    if (
        ball.xcor() < -320
        and ball.xcor() > -350
        and abs(ball.ycor() - left_paddle.ycor()) < 50
    ):

        ball.bounce_x()


    # -------------------------
    # Right player misses
    # -------------------------

    if ball.xcor() > 390:

        scoreboard.left_point()

        ball.reset_position()


    # -------------------------
    # Left player misses
    # -------------------------

    if ball.xcor() < -390:

        scoreboard.right_point()

        ball.reset_position()


    # -------------------------
    # Check winner
    # -------------------------

    if (
        scoreboard.left_score >= 5
        or scoreboard.right_score >= 5
    ):

        game_running = False


scoreboard.game_winner()

screen.exitonclick()
