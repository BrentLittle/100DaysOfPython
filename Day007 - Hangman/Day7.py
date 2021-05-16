### Project Day ###

# The goal of today is to create the code version of Hangman

# This will work the same way the regular game of hangman should work
    # You guess a letter, if it is wrong a body part is added to the hanging man
    # if it is a letter that is within the word to be guessed it is displayed to the player to give them more information as to what the hidden word is


## hangmanwordgame.com
import random

wordList = ["aardvark", "baboon", "camel"]
randWord = random.choice(wordList)
display = ['_'] * len(randWord)
lettersGuessed = []
lives = 6
 

while True:
    userGuess = input("Please Guess a letter: ").lower()
    letterCorrect = False
    for index in range(0,len(display)):
        if userGuess == randWord[index]:
            display[index] = randWord[index]
            letterCorrect = True
        
    if not letterCorrect:
        lives-=1
        
    lettersGuessed.append(userGuess)
    
    print(f"Hidden Word: {' '.join(display)}")
    print(f"Letters Guessed: {' '.join(lettersGuessed)}")
    print(f"Lives Remaining: {lives}")


    if (lives != 0) and ("_" not in display):
        print("You Win")
        break
    elif (lives == 0):
        print("Game Over")
        print(f"The Correct word was: {randWord}")
        break

    print("\n\n\n")
