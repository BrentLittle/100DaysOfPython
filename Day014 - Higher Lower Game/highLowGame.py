import os
import random
from data import data

clear = lambda: os.system("cls")

def getRandomData():
    return data[random.randint(0,len(data)-1)]

def isUserCorrect(userGuess, optA, optB):
    if userGuess == "a" and (optA["follower_count"] >= optB["follower_count"]):
        return True
    elif userGuess == "b" and (optA["follower_count"] <= optB["follower_count"]):
        return True
    else:
        return False

def game():
    print("Welcome to Higher or Lower. The goal of this game is to guess who has more followers.")
    print("Lets Begin!")
    
    score = 0

    optionA = getRandomData()
    optionB = getRandomData()

    gameOver = False
    while not gameOver:
        print(f"Compare A: {optionA['name']}, a {optionA['description']}, from {optionA['country']}  Hint: {optionA['follower_count']}")
        print(f"Against B: {optionB['name']}, a {optionB['description']}, from {optionB['country']}  Hint: {optionB['follower_count']}")

        selection = input("Who has more Followers? Type 'A' or 'B': ").lower()

        if isUserCorrect(selection, optionA, optionB):
            # clear()
            score += 1
            print(f"You are correct! Your current score is: {score}")
            if selection == "a":
                optionB = getRandomData()
            else:   
                optionA = optionB
                optionB = getRandomData()

        else:
            clear()
            print(f"Sorry that is wrong. Your final Score was: {score}")
            gameOver = True


clear()
game()