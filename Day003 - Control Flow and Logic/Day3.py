# ### If / If-Else control ###
# waterLvl = 50
# if waterLvl > 80:
#     print("Draining Water")
# else:
#     print("Filling Up")

# print("Welcome to the rollercoaster Ride")
# height = int(input("Please Enter Your Height in cm: "))
# if height >= 120:
#     print("Can Ride the Coaster")
# else:
#     print("Cant Ride the Coaster")


# ### Coding Expercise 1 ###
# # Write a program that works out whether if a given number is an odd or even number.
# numberInput = int(input("Please enter ANY number: "))
# if numberInput % 2 == 0:
#     print(f"{numberInput} Is Even")
# else:
#     print(f"{numberInput} Is Odd")


# ### Nested If Statements and elif statements ###
# print("Welcome to the rollercoaster Ride")
# height = int(input("Please Enter Your Height in cm: "))
# age = int(input("Please Enter Your Age: "))
# if height >= 120:
#     print("Can Ride the Coaster")
#     if age > 18:
#         print("Must Pay $12")
#     elif ((12 <= age) and (age <= 18)):
#         print("Must Pay $7")
#     else:
#         print("Must Pay $5")
# else:
#     print("Cant Ride the Coaster")


# ### Coding Expercise 2 ###

# # Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# # It should tell them the interpretation of their BMI based on the BMI value.

# # - Under 18.5 they are underweight
# # - Over 18.5 but below 25 they have a normal weight
# # - Over 25 but below 30 they are slightly overweight
# # - Over 30 but below 35 they are obese
# # - Above 35 they are clinically obese.

# # The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# height = float(input("Please Enter Your Height in m: "))
# weight = float(input("Please Enter Your Weight in Kg: "))
# bmi = round(weight/(height**2))

# if(bmi < 18.5):
#     print("You are Underweight")
# elif(bmi < 25):
#     print("You have a normal weight")
# elif(bmi < 30):
#     print("You are slightly overweight")
# elif(bmi < 35):
#     print("You are obese")
# else:
#     print("You are clinically obese")


# ### Coding Expercise 3 ###
# # Write a program that works out whether if a given year is a leap year.
# # This is how you work out whether if a particular year is a leap year.

# #  `on every year that is evenly divisible by 4
# #    **except** every year that is evenly divisible by 100
# #      **unless** the year is also evenly divisible by 400`
# year = int(input("Please Enter a Year: "))

# if(year % 4 == 0):
#     if(year % 100 == 0):
#         if(year % 400 == 0):
#             print("Leap Year!")
#         else:
#             print("Not a Leap Year")
#     else:
#         print("Not a Leap Year")
# else:
#     print("Not a Leap Year")


# ### Coding Expercise 4 ###
# print("Welcome to Python Pizza!")
# orderTotal = 0
# size = input("What Size of Pizza Would You like? S, M, or L").upper()
# peperoniAdded = input("Would you like Pepperoni on your pizza? Y or N?").upper()
# extraCheese = input("Would you like extra Cheese? Y or N?").upper()

# if (size == "S"):
#     orderTotal += 15
# elif (size == "M"):
#     orderTotal += 20
# elif (size == "L"):
#     orderTotal += 25

# if peperoniAdded == "Y":
#     if size == "S":
#         orderTotal += 2
#     elif size == "M" or size == "L":
#         orderTotal += 3

# if extraCheese == "Y":
#     orderTotal += 1

# print(f"Your Order Total Will be: ${orderTotal}")


### Coding Expercise 5 ###
# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.

name1 = input("Enter the first name: ").upper()
name2 = input("Enter the second name: ").upper()

score = 0
combination = name1+name2

score += 10 * combination.count("T") 
score += 10 * combination.count("R") 
score += 10 * combination.count("U") 
score += 10 * combination.count("E") + combination.count("E")

score += combination.count("L") 
score += combination.count("O") 
score += combination.count("V") 

if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >=40 and score <=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")