from turtle import Turtle
# initializing basic functions
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(-180,250)
        self.write_score()

# refreshes score
    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}\nHighscore: {self.highscore}", align="left", font=("Courier", 12, "normal"))
# adds 1 to current score
    def add_score(self):
        self.score +=1
        self.write_score()

# post-game ending screen + writing high score to save file
    def game_over(self):
        self.goto(0,0)
        if self.score > self.highscore:
            self.highscore = self.score
            self.write(f"GAME OVER", align="center", font=("Courier", 12, "normal"))
            self.goto(0, -16)
            self.write(f"New high score:{self.highscore}", align="center", font=("Courier", 12, "normal"))
            with open("highscore.txt", "w") as data:
                data.write(str(self.highscore))
        elif self.score <= self.highscore:
            self.write(f"GAME OVER \nScore:{self.score}", align="center", font=("Courier", 12, "normal"))