from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameOn = True
while gameOn:
    screen.update()
    time.sleep(0.15)
    snake.move()
    
    # Collision with food checking
    if snake.segments[0].distance(food) < 15:
        food.updateLoc()
        scoreboard.increaseScore()
        snake.grow()

    # Detect Collision with Wall
    if snake.segments[0].xcor()<-290 or snake.segments[0].xcor()>290 or snake.segments[0].ycor()<-290 or snake.segments[0].ycor()>290:
        gameOn = False
        scoreboard.gameIsOver()

    # Detect Collision with Tail
    for seg in snake.segments[1:]:
        if snake.segments[0].distance(seg) < 5:
            gameOn = False
            scoreboard.gameIsOver()
    

    
    
    


screen.exitonclick()