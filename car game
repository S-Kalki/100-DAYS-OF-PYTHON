from turtle import Screen
import time

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("lightgreen")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_on = True

while game_on:

    time.sleep(0.08)
    screen.update()

    cars.create_car()
    cars.move_cars()

    for car in cars.cars:
        if player.distance(car) < 20:
            game_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.reset()
        cars.increase_speed()
        scoreboard.next_level()

screen.exitonclick()
