from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10

    def move(self):
        self.goto(self.xcor()+self.xmove, self.ycor()+self.ymove)

    def bounceY(self):
        self.ymove *= -1

    def bounceX(self):
        self.xmove *= -1

    def resetPosition(self):
        self.goto(0,0)
        self.bounceX()