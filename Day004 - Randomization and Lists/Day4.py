### Randomization ###
# Python has a built in module for random actions
import random

# We can also import other python files as modules as well.
# import Day4Module
# print(Day4Module.pi)

randomInt = random.randint(1,10)
print(randomInt)

radomFloat = random.random()
print(radomFloat)




### Code Challenge 1 ###
# You are going to write a virtual coin toss program. 
# It will randomly tell the user "Heads" or "Tails". 

# e.g.
# 1 means Heads
# 0 means Tails

HorT = random.randint(0,1)
if HorT == 1:
    print("You Flipped Heads")
else:
    print("You Flipped Tails")




### Python Lists ###
# Python Lists are a data structure to organize and store multiple pieces of data to be grouped together.
formulaSeries = ["F1", "F2", "F3"]

# Lists have an order to them i.e. ontario is first followed by NS in second, etc...
canadianProvinces = ["Ontario", "Nova Scotia", "New Brunswick", "British Columbia"]

# Use the name of the list followed by square brackets to obtain items from the list
print(canadianProvinces[0])
print(canadianProvinces[-1])

canadianProvinces.append("P.E.I")
print(canadianProvinces[-1])

canadianProvinces.extend(["Quebec", "Manitoba", "Saskatchewan"])
print(canadianProvinces)




### Coding Challenge 2 ###
# You are going to write a program which will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.

namesString = input("Give me everybody's names, separated by a comma. ")
names = namesString.split(", ")
nameSelection = names[random.randint(0,len(names)-1)]
print(f"{nameSelection} is going to buy the meal today!")




### Nested Lists ###
drivers = ["Hamilton","Bottas", "Verstappen", "Perez", "Norris"]
teams = ["Mercedes", "Redbull", "McLaren", "Ferrari", "Williams"]

nestedList = [drivers,teams]

print(nestedList)
print(nestedList[0][0])




### Coding Exercise 3 ###
# You are going to write a program which will mark a spot with an X
# Your job is to write a program that allows you to mark a square on the map using a two-digit system. 
# The first digit is the vertical column number 
# and the second digit is the horizontal row number. e.g.:

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
col = int(position[0]) - 1
row = int(position[1]) - 1
map[row][col] = "X"

print(f"{row1}\n{row2}\n{row3}")