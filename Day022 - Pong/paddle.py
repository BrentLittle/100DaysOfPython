from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(location[0],location[1])

    def goUp(self):
        self.goto(self.xcor(), self.ycor()+20)
    
    def goDown(self):
        self.goto(self.xcor(), self.ycor()-20)