from turtle import Turtle


STARTING_POSITIONS = [
    (0, 0),
    (-20, 0),
    (-40, 0)
]

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):

        self.segments = []

        self.create_snake()

        self.head = self.segments[0]

    # -----------------------------
    # Create initial snake
    # -----------------------------

    def create_snake(self):

        for position in STARTING_POSITIONS:

            self.add_segment(position)

    # -----------------------------
    # Add a new segment
    # -----------------------------

    def add_segment(self, position):

        segment = Turtle("square")

        segment.color("lime")
        segment.penup()

        segment.goto(position)

        self.segments.append(segment)

    # -----------------------------
    # Grow snake
    # -----------------------------

    def grow(self):

        last_position = self.segments[-1].position()

        self.add_segment(last_position)

    # -----------------------------
    # Move snake
    # -----------------------------

    def move(self):

        # Move body segments first
        for number in range(
            len(self.segments) - 1,
            0,
            -1
        ):

            new_x = self.segments[number - 1].xcor()
            new_y = self.segments[number - 1].ycor()

            self.segments[number].goto(
                new_x,
                new_y
            )

        # Move head
        self.head.forward(MOVE_DISTANCE)

    # -----------------------------
    # Direction controls
    # -----------------------------

    def up(self):

        if self.head.heading() != DOWN:

            self.head.setheading(UP)

    def down(self):

        if self.head.heading() != UP:

            self.head.setheading(DOWN)

    def left(self):

        if self.head.heading() != RIGHT:

            self.head.setheading(LEFT)

    def right(self):

        if self.head.heading() != LEFT:

            self.head.setheading(RIGHT)