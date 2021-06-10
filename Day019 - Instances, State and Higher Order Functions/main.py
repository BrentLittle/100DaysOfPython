from turtle import Turtle, Screen
# Event Listeners for Turtle
"""

"""

turtle = Turtle()
screen = Screen()

def moveForward():
    turtle.forward(10)

screen.listen()
screen.onkey(key="space", fun=moveForward)
screen.exitonclick()