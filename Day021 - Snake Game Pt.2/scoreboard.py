from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=265)
        self.writeScore()
        

    def increaseScore(self):
        self.score += 1
        self.writeScore()

    def writeScore(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font = ("Arial", 24, "normal"))

    
    def gameIsOver(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", align="center", font = ("Arial", 24, "normal"))