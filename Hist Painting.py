import turtle as turtle_module
import random

turtle_module.colormode(255)

color_list = [
    (202, 165, 109),
    (149, 75, 50),
    (222, 201, 137),
    (52, 93, 124),
    (63, 46, 42),
    (140, 170, 154)
]

tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for y in range(10):

    for x in range(10):

        tim.dot(20, random.choice(color_list))
        tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

turtle_module.Screen().exitonclick()