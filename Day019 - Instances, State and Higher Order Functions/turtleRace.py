from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width = 500, height = 400)
isRaceOn = False
userBet = screen.textinput(title = "Make a Bet", prompt = "Enter a color: ")

turtleColors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtleObjects = []

xLoc, yLoc = -230, -100
for color in turtleColors:
    turtle = Turtle(shape = "turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x = xLoc, y = yLoc)
    turtleObjects.append(turtle)
    yLoc += 40

if userBet:
    isRaceOn = True

while isRaceOn:
    for turtle in turtleObjects:
        turtle.forward(random.randint(0,10))
        if turtle.xcor() > 230:
            isRaceOn = False
            if turtle.color() == userBet.lower():
                print("You Win!")
            else:
                print("Thanks for playing!") 
            print(f"The Winner of the Race was the {turtle.color()[0]} turtle")

screen.exitonclick()