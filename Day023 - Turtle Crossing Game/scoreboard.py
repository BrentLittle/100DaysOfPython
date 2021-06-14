from turtle import Turtle

FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.updateLevel()

    def updateLevel(self):
        self.clear()
        self.level += 1
        self.goto(x= -215, y= 260)
        self.write(f"Level: {self.level}", align = "center", font=FONT)


    def gameOver(self):
        self.goto(x= 0, y= 0)
        self.write(f"GAME OVER", align = "center", font=FONT)
