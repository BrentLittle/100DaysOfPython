from turtle import Turtle, Screen
import random as rand
import colorgram

turtle = Turtle()

listOfColors=[]
colors = colorgram.extract('hirstImg.jpg', 20)
for color in colors:
    listOfColors.append(( color.rgb.r, color.rgb.g, color.rgb.b))

rows, cols = 10, 10
dotSize = 20
dotSpacing = 50

turtle.penup()
turtle.setpos(turtle.pos()[0] - 225, turtle.pos()[1] - 225)

for i in range(rows):
    for j in range(cols):
        color = rand.choice(listOfColors)
        turtle.dot(dotSize, (color[0]/255, color[1]/255, color[2]/255))
        turtle.forward(dotSpacing)
    turtle.setpos(turtle.pos()[0] - 500, turtle.pos()[1] + dotSpacing)
    







screen = Screen()
screen.exitonclick()