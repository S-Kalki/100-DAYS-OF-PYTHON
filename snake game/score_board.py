from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()

        self.score = 0
        self.high_score = 0

        self.color("white")

        self.penup()

        self.goto(0, 320)

        self.hideturtle()

        self.update_score()

    # -----------------------------
    # Display score
    # -----------------------------

    def update_score(self):

        self.clear()

        self.write(
            f"Score: {self.score}    "
            f"High Score: {self.high_score}",
            align="center",
            font=("Arial", 18, "bold")
        )

    # -----------------------------
    # Increase score
    # -----------------------------

    def increase_score(self, points):

        self.score += points

        if self.score > self.high_score:

            self.high_score = self.score

        self.update_score()

    # -----------------------------
    # Game over
    # -----------------------------

    def game_over(self):

        self.goto(0, 30)

        self.write(
            "GAME OVER",
            align="center",
            font=("Arial", 30, "bold")
        )

        self.goto(0, -20)

        self.write(
            f"Final Score: {self.score}",
            align="center",
            font=("Arial", 18, "normal")
        )

        self.goto(0, -60)

        self.write(
            "Press R to play again",
            align="center",
            font=("Arial", 14, "normal")
        )

    def restart_message(self):

        print("Restart the program to play again.")