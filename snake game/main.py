from turtle import Screen
import time

from snake import Snake
from food import Food
from score_board import Scoreboard


WIDTH = 700
HEIGHT = 700

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


# Controls
screen.listen()

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

# Arrow keys also work
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_running = True


while game_running:

    screen.update()

    # Game gets faster as score increases
    delay = max(0.05, 0.13 - scoreboard.score * 0.004)

    time.sleep(delay)

    snake.move()


    # -----------------------------
    # Food collision
    # -----------------------------

    if snake.head.distance(food) < 18:

        snake.grow()

        scoreboard.increase_score(food.points)

        food.refresh()


    # -----------------------------
    # Wall collision
    # -----------------------------

    if (
        snake.head.xcor() > 335
        or snake.head.xcor() < -335
        or snake.head.ycor() > 335
        or snake.head.ycor() < -335
    ):

        game_running = False


    # -----------------------------
    # Self collision
    # -----------------------------

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:

            game_running = False

            break


# Game over
if not game_running:

    scoreboard.game_over()

    screen.exitonclick()
