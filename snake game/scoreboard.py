from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        high_score_file = open("highscore.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        self.high_score = high_score
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        if self.score > self.high_score:
            new_highscore = self.score
            highscore_file = open("highscore.txt", "w")
            highscore_file.write(f"{new_highscore}")
            highscore_file.close()


        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

