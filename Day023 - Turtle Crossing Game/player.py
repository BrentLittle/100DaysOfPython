from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goToStartingLoc()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def goToStartingLoc(self):
        self.goto(STARTING_POSITION)

    def reachedFinish(self):
        return self.ycor() > FINISH_LINE_Y
