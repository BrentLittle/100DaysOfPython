from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.listen()

def forwards():
    turtle.forward(10)

def backwards():
    turtle.forward(-10)

def right():
    turtle.setheading(turtle.heading() + 10)

def left():
    turtle.setheading(turtle.heading() - 10)

def clear():
    screen.reset()


screen.onkey(forwards, "w")
screen.onkey(backwards,"s")
screen.onkey(left, "a")
screen.onkey(right, "d")
screen.onkey(clear, "c")

screen.exitonclick()