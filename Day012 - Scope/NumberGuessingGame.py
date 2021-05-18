import os
import random

clear = lambda: os.system("cls")
clear()

def randomNum():
    return random.randint(1,100)

def decreaseGuesses():
    return guesses - 1

def checkGuess():
    if guess < selectedNum:
        return 1
    elif guess > selectedNum:
        return 2
    else:
        return 3


print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100")

selectedNum = randomNum()

print(f"Hint: The number that I selected was {selectedNum}")

difficulty = input("Choose a difficulty. Type 'easy' for 10 guesses or 'hard' for 5 guesses: ").lower()

guesses = 5
if difficulty == "easy":
    guesses = 10


won = False
while True:
    print(f"You have {guesses} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))

    checkVal = checkGuess()

    if checkVal == 1:
        print("Too Low")
        guesses = decreaseGuesses()
    elif checkVal == 2:
        print("Too High")
        guesses = decreaseGuesses()
    else:
        won = True
        break

    if guesses == 0:
        print("You have run out of guesses")
        break


if won:
    print(f"You got it! The correct answer was {selectedNum}")
else:
    print(f"Game Over, The correct answer was {selectedNum}")
