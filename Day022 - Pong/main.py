from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

left = Paddle((-350,0))
right = Paddle((350,0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(right.goUp,"Up")
screen.onkey(right.goDown,"Down")
screen.onkey(left.goUp,"w")
screen.onkey(left.goDown,"s")

gameOn = True
while gameOn:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect Collision with Top/Bottom Walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    # Detect collision with right Paddle
    if ball.distance(right)<50 and ball.xcor()>320 or ball.distance(left)<50 and ball.xcor()<-320 :
        ball.bounceX()

    # Detect a left paddle score
    if ball.xcor() > 380:
        ball.resetPosition()
        scoreboard.giveLeftPoint()

    # Detect a Right paddle score
    if ball.xcor() < -380:
        ball.resetPosition()
        scoreboard.giveRightPoint()


screen.exitonclick()

