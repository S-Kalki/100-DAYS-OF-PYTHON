from turtle import Turtle,Screen
oreo=Turtle()
my_screen=Screen()
print(oreo)
oreo.shape("turtle")
oreo.color("red")
#Draw a Square
for i in range(4):
    oreo.forward(100)
    oreo.right(90)


#Dashed line
for i in range(5):
    oreo.forward(20)
    oreo.penup()
    oreo.forward(20)
    oreo.pendown()

#Shapes
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "gold", "violet"]
for i in range(3,10):
    for j in range(i):
        oreo.color(colors[i-3])
        oreo.forward(100)
        oreo.right(360/i)

#rando, walk
import random
directions = [0, 90, 180, 270]
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "gold", "violet"]
for i in range(100):
    oreo.color(colors[i % len(colors)])
    oreo.forward(50)
    oreo.setheading(random.choice(directions))
my_screen.colormode(255)
angle=0
while angle<361:
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    oreo.color(r,g,b)
    oreo.circle(100)
    oreo.setheading(angle)
    angle+=20




my_screen=Screen()
print(my_screen.canvheight)
my_screen.exitonclick()