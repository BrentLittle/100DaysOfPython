print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
LorR = input("Where would you like to go? Left or Right? ").lower()

if(LorR != "left"):
    print("Oh No! you fell into a hole")
    print("Game Over.")
    quit()

print("Your Decided to go left, Good Choice!")
SorW = input("You are met with a river with lots of fish do you ... Swim or Wait? ").lower()

if(SorW != "wait"):
    print("Oh No! you were visciously attacked by a Trout")
    print("Game Over.")
    quit()

print("You decided to wait and take in your surroundings, You notice three coloured doors to your left.")
doorSelection = input("Whihc door do you select? Red, Blue, or Yellow? ").lower()

if doorSelection =="red":
    print("Oh No! you were burned by fire")
    print("Game Over.")
    quit()
elif doorSelection == "blue":
    print("Oh No! you were eaten by beasts")
    print("Game Over.")
    quit()
elif doorSelection == "yellow":
    print("YOU WIN!")
    quit()
else:
   print("Game Over.")
   quit() 