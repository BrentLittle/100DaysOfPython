import os

clear = lambda: os.system("cls")
clear()

## Scope ##

enemies = 1
def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")




## Local Scope ##
def drinkLocal():
    potionStrength = 2   # This is a Local variable to the drinkLocal Funciton and cannot be used outside the scope of the function  
    print(potionStrength)

drinkLocal()
# print(potionStrength)




## Global Scope ##
health = 10 # This is a global variable and can be utilized anywhere in the python file as it has a global scope
def drinkGlobal():
    potionStrength = 2
    print(health)

drinkGlobal()

# Scope also applies to functions and anything else named
# This concept is called Namespace




## Modifying within global scope ##

enemies = 1
# BAD WAY
# def increaseEnemies():
#     global enemies
#     enemies+=1
#     print(f"enemies inside function: {enemies}")

# increaseEnemies()
# print(f"enemies outside function: {enemies}")


# GOOD WAY
def increasEnemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1
enemies=increasEnemies()
print(f"enemies outside function: {enemies}")




## Global Constants ##

PI = 3.14159
URL= "https://www.google.com"



