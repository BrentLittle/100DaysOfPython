from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.movementSpeed = STARTING_MOVE_DISTANCE
        self.allcars = []

    def createNewCar(self):
        car = Turtle()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        yLoc = random. randint(-250, 250)
        car.goto(300, yLoc)
        car.setheading(180)
        self.allcars.append(car)

    def moveCars(self):
        for car in self.allcars:
            car.forward(self.movementSpeed)   

    def incrementSpeed(self):
        self.movementSpeed += MOVE_INCREMENT
