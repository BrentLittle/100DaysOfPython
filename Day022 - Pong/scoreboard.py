from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.leftScore = 0
        self.rightScore = 0
        self.updateScoreboard()
        

    def updateScoreboard(self):
        self.clear()

        self.goto(x= -100, y= 200)
        self.write(self.leftScore, align = "center", font=("Courier", 80, "normal"))

        self.goto(x= 100, y= 200)
        self.write(self.rightScore, align = "center", font=("Courier", 80, "normal"))

    def giveLeftPoint(self):
        self.leftScore += 1
        self.updateScoreboard()

    def giveRightPoint(self):
        self.rightScore += 1
        self.updateScoreboard()