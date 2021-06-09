from turtle import Turtle, Screen
import random as rand

turtle = Turtle()

# turtle.shape("arrow")
# turtle.color("azure4")
# turtle.forward(100)
# turtle.right(90)





### Challenge 1: Draw a Square
# for _ in range(4):
#     turtle.forward(100)
#     turtle.right(90)





"""
importing modules

import keyword (ex. import turtle)
With this we would need to do the following to create a new object of type Tutle
tim = turtle.Turtle()


from moduleName import itemInModule (ex. from turtle import Turtle)
With this we would need to do the following to create a new object of type Tutle
tim = Turtle()


We cna also import all items in a module using the * attribute
from turtle import *


We are also able to alias modules using the following form:
import moduleName as aliasName (ex. import turtle as t)
"""





### Challenge 2: Draw a dashed line
# for _ in range(15):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()





### Challenge 3: Draw shapes from numsides of 3 to 10
# for i in range(3, 11):
#     angle = 360 / i
#     turtle.color(rand.random(), rand.random(), rand.random())
#     for x in range(i):
#         turtle.forward(100)
#         turtle.right(angle)





### Challenge 4: Generate a random Walk
# directions = [0, 90, 180, 270]
# turtle.pensize(10)
# turtle.speed("fastest")
# for _ in range(200):
#     turtle.color(rand.random(), rand.random(), rand.random())
#     turtle.setheading(rand.choice(directions))
#     turtle.forward(30)





### Challenge 5: Generate a Spirograph
turtle.speed("fastest")
numOfCircles = 100
for _ in range(numOfCircles):
    turtle.color(rand.random(), rand.random(), rand.random())
    turtle.circle(100)
    turtle.setheading(turtle.heading() + 360/numOfCircles)






screen = Screen()
screen.exitonclick()