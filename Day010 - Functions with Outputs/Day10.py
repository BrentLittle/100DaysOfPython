import os

clear = lambda: os.system("clear")
clear()

## Funcitons can also return values in their execution.
def formatName(firstName, lastName):
    return f"{firstName.title()} {lastName.title()}"


print(formatName("brent", "littlefield"))


## Multiple Return Values
def formatNameMultiple(firstName, lastName):

    if firstName == "" or lastName == "":
        return "Invalid Inputs provided"
    return f"Result: {firstName.title()} {lastName.title()}"


print(formatNameMultiple("brent", "littlefield"))


### Coding Challenge 1 ###

# You are then going to create a function called days_in_month() which will take a year and a month as inputs,
# And it will use this information to work out the number of days in the month, then return that as the output


def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def daysInMonth(year, month):
    daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12 or month < 1:
        return "Invalid Month"
    if month == 2 and isLeapYear(year):
        return 29
    else:
        return daysInMonths[month - 1]
