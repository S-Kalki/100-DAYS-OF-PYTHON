from turtle import Turtle
import random


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = 5

    def create_car(self):
        if random.randint(1, 6) == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice([
                "red", "blue", "orange",
                "yellow", "purple", "black"
            ]))

            y = random.randint(-240, 240)
            car.goto(320, y)

            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed += 1