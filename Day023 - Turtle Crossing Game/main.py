import time
from turtle import Screen
from player import Player
from carManager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move,"Up")

carManager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
loopCounter = 0

while game_is_on:
    # Check if Player Hit top of screen
    if player.reachedFinish():
        player.goToStartingLoc()
        scoreboard.updateLevel()
        carManager.incrementSpeed()

    # Generate new car every 6th loop
    if loopCounter % 6 == 0:
        carManager.createNewCar()
    
    # check for collision between a car and Player
    for car in carManager.allcars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameOver()

    # move all the cars
    carManager.moveCars()

    time.sleep(0.1)
    screen.update()
    loopCounter += 1


screen.exitonclick()

