# ### Loops with Lists ###

# #For Loop#
# # for item in listOfItems:
#     # do something

fruits=["Apple","Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)




### Coding Exercise 1 ###
# You are going to write a program that calculates the average student height from a List of heights.
studentHeights = [180, 124, 165, 173, 189, 169, 146]
totalHeight = 0
for height in studentHeights:
    totalHeight += height

avgHeight = totalHeight/len(studentHeights)
print(f"The Average height was: {round(avgHeight)} cm.")




### Coding Exercise 2 ###
# You are going to write a program that calculates the highest score from a List of scores. 
studentScores = [78, 65, 89, 86, 55, 91, 64, 89]
highScore = -1 # This is an assumption that you cannot get lower than a 0 for a score
for score in studentScores:
    if score > highScore:
        highScore = score
print(f"The highest score in the class is: {highScore}")




### Loops with a Range() ###
# for number in range(a,b):
#     do something with each number from a up to but not including b
#     [a,b)

for number in range(1,10):
    print(number)

# This loop has a step size of 3
for number in range(1,10,3):
    print(number)

accum = 0
for number in range(1,101):
    accum += number
print(accum)




### Coding Exercise 3 ###
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. 
# Thus, the first even number would be 2 and the last one is 100:
total = 0
for num in range(1,101):
    if num % 2 == 0:
        total += num
print(total)




### Coding Exercise 4 ###
# You are going to write a program that automatically prints the solution to the FizzBuzz game. 
# Your program should print each number from 1 to 100 in turn. 
# When the number is divisible by 3 then instead of printing the number it should print "Fizz". 
# When the number is divisible by 5, then instead of printing the number it should print "Buzz". 
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for val in range(1,21):
    if val%3==0 and val%5==0:
        print("FizzBuzz")
    elif val%3==0:
        print("Fizz")
    elif val%5==0:
        print("Buzz")
    else:
        print(val)
