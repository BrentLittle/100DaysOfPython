### Data Types ###
 
## Strings
# Strings are an array of individual characters
print("Hello"[1])
print("Hello"[-1])
print("123"+"345")

## Integer
# Number with no decimal (whole number)
print(123+345)

## Floating point
# numbers with a decimal value
print(3.141592653859)

## Boolean Value
# Data type with two possible values True or False
print(True)
print(False)





### Type Casting ###

numChar = len(input("Enter Your Name:"))
print(type(numChar))
# print("Your name has " +numChar+ " letters") THIS DOES NOT WORK DUE TO AN INT NOT BEING ABLE TO CONCATENATED WITH STRINGS
print("Your name has " +str(numChar)+ " letters")

a=123
print(type(a))

a=str(123)
print(type(a))

print(70+float(100.5))
print(str(70)+str(100))





### Challenge ###
# Write a program that adds the digits in a 2 digit number. 
# e.g. if the input was 35, then the output should be 3 + 5 = 8
num = input("Enter a 2 Digit Number")
print( int(num[0]) + int(num[1]))





### Mathematical Operation ###
#Addition           +
#Subtraction        -
#Multiplication     *
#Division           /   
#Exponent           **

# BEDMAS is followed for priority in Python





### Code Challenge ###

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# The BMI is a measure of some's weight taking into account their height. 
# e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
height = float(input("Enter Your height in m: \n"))
weight = float(input("Enter Your weight in Kg: \n"))

bmi = int(weight/height**2)
print(bmi)





### Number Conversion and String Manipulation ###
div = 8/3
print(round(div))
print(round(div,2))

# Floor Division
print(8//3)

# F Strings
score = 0
height = 1.8
winner=False
print(f"Your Score is: {score}, \nYour height is: {height}, \nAre you Winning Son? {winner}")





### Coding Challenge ###

#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left 
# if we live until 90 years old. 
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left. 
# Where x, y and z are replaced with the actual calculated numbers. 

age = int(input("How Old are you in years? \n"))
print(f"you have {(90-age) * 365} days left, or {(90-age) * 52} weeks left or {(90-age) * 12} months left, However you want to look at it. ")