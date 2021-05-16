## Functions with Inputs ##
def greetPerson( nameOfPerson ):
    print(f"Good morning {nameOfPerson}, How are you today?")


greetPerson("Brent Littlefield")
greetPerson("Kyle")

## nameOfPerson is a parameter where as the data we pass to the function is the argument.



### Positional vs Keyword Arguments ###
def specificGreeting(name, location):
    print(f"Good morning {name}, How are you today?")
    print(f"What is it like in {location}?")


specificGreeting("Brent","Canada")


# With keyword arguments we can add the parameter names to name sure that the positioning of the variables is unaffected

specificGreeting(name="Brent",location="Canada")
specificGreeting(location="Canada",name="Brent")


## Coding Exercise 1 ##
#The instructions on the paint can says that **1 can of paint can cover 5 square meters** of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

#number of cans = (wall height ✖️ wall width) ÷ coverage per can. 
def numOfPaintCans(width, height):
    area = width*height
    numCans = round(area/5)
    print(f"You Need to buy {numCans} cans of paint for the wall")


width = float(input("Enter width of wall:"))
height= float(input("Enter height of wall:"))
numOfPaintCans(width, height)


## Coding Exercise 2 ## 
#You need to write a function that checks whether if the number passed into it is a prime number or not.
import math
def isPrime(n):
    if n == 2:
        print("Prime")
    if n % 2 == 0 or n <= 1:
        print("Not Prime")

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            print("Not Prime")
            return
    print("Prime")

isPrime(1)
isPrime(2)
isPrime(3)
isPrime(4)
isPrime(5)
isPrime(7)
isPrime(9)
isPrime(11)