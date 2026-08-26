from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):

        super().__init__()

        self.penup()
        self.speed("fastest")

        self.points = 1

        self.refresh()

    def refresh(self):

        random_x = random.randint(-320, 320)
        random_y = random.randint(-320, 320)

        self.goto(random_x, random_y)

        # 20% chance of bonus food
        if random.randint(1, 5) == 1:

            self.shape("circle")
            self.color("gold")

            self.shapesize(
                stretch_wid=0.8,
                stretch_len=0.8
            )

            self.points = 3

        else:

            self.shape("circle")
            self.color("red")

            self.shapesize(
                stretch_wid=0.5,
                stretch_len=0.5
            )

            self.points = 1