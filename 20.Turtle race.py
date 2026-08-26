from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win? Enter a color: "
)

turtles = []

y_position = -100

for color in colors:

    turtle = Turtle(shape="turtle")
    turtle.color(color)

    turtle.penup()
    turtle.goto(x=-230, y=y_position)

    y_position += 40

    turtles.append(turtle)


race_on = True

while race_on:

    for turtle in turtles:

        if turtle.xcor() > 230:

            race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")

            else:
                print(
                    f"You lost! The {winning_color} turtle is the winner!"
                )

            break

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()