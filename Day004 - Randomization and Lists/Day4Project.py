import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock , paper, scissors]
print("What do you choose?")
userSelection = int(input("1 for Rock \n2 for Paper \n3 for Scissors \n"))
print(choices[userSelection-1])

print("Computer Chose:")
compSelection = random.randint(1,3)
print(choices[compSelection-1])

## Game Logic to Determine who wins

# Rock Wins over Scissors       1 beats 3
# Paper Wins over Rock          2 beats 1
# Scissors wins over Paper      3 beats 2

if (userSelection == 1 and compSelection == 3)or(userSelection == 2 and compSelection == 1)or(userSelection == 3 and compSelection == 2):
    print("You Win")
elif (userSelection == 3 and compSelection == 1)or(userSelection == 1 and compSelection == 2)or(userSelection == 2 and compSelection == 3):
    print("You Lose")
else:
    print("It was a Tie")