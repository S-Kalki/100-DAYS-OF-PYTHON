from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("yellow")

        self.penup()

        self.x_speed = 5
        self.y_speed = 5

    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed

        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_speed *= -1

    def bounce_x(self):
        self.x_speed *= -1

        # Make the ball slightly faster
        if self.x_speed > 0:
            self.x_speed += 0.5
        else:
            self.x_speed -= 0.5

    def reset_position(self):

        self.goto(0, 0)

        self.x_speed = -5 if self.x_speed > 0 else 5
        self.y_speed = 5