### Dictionaries ###

# Dictionaries have a key and a value that goes along with the key.

# Dictionaries have key-value pairs
# {key:value}
# {"Bug": "An error in a program that prevents the program from runing as expected"}

# a list of these key value pairs create a dictionary
# {{key:value}, {key:value}, {key:value}}

# declaring a Distionary
from typing import Dict


dict = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of repeating something",
}

# referencing data in dictionary
# print(dict["Bug"])

# adding new items to Dictionary
dict["Python"] = "The best programming language"
# print(dict)

# starting with empty list
emptyDict = {}

# clearing dictionary
# dict = {}

# editing informaiton in a dicitonary
dict["Bug"] = "A not good situation to have"
# print(dict)

# Looping through dictionary
for key in dict:
    print(f"{key}: {dict[key]}")


### Coding Challenge 1 ###

# You have access to a database of student_scores in the format of a dictionary.
# The keys in student_scores are the names of the students and the values are their exam scores.

# Write a program that converts their scores to grades.
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

studentScores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

studentGrades = {}

for student in studentScores:
    grade = studentScores[student]
    if grade <= 70:
        studentGrades[student] = "Fail"
        continue
    elif grade >= 71 and grade <= 80:
        studentGrades[student] = "Acceptable"
        continue
    elif grade >= 81 and grade <= 90:
        studentGrades[student] = "Exceeds Expectations"
        continue
    else:
        studentGrades[student] = "Outstanding"

# print(studentGrades)


### Nesting Lists and Dictionaries ###

# The values for keys in a dictionary can also be lists or dictionaries as well

# {
#     {key, [List]},
#     {key2, {Dict}},
# }


capitalCities = {
    "Canada": "Ottawa",
    "Netherlands": "Amsterdam",
    "France": "Paris",
}

# Nesting a list in a Dcitionary
myTravelsDictList = {
    "Canada": ["Kingston", "Guelph", "Waterloo", "Kitchener", "Toronto", "Ottawa"],
    "Netherlands": ["Amsterdam", "Haarlem", "Rotterdam", "De Haag"],
}

# Nesting a Dictionary in a Dcitionary
myTravelsDictDict = {
    "Canada": {
        "citiesVisited": [
            "Kingston",
            "Guelph",
            "Waterloo",
            "Kitchener",
            "Toronto",
            "Ottawa",
        ],
        "visits": 150,
    },
    "Netherlands": {
        "citiesVisited": ["Amsterdam", "Haarlem", "Rotterdam", "De Haag"],
        "visits": 1,
    },
}


# Nesting Dict in a List
myTravelsListDict = [
    {
        "country": "Canada",
        "citiesVisited": [
            "Kingston",
            "Guelph",
            "Waterloo",
            "Kitchener",
            "Toronto",
            "Ottawa",
        ],
        "visits": 150,
    },
    {
        "country": "Netherlands",
        "citiesVisited": ["Amsterdam", "Haarlem", "Rotterdam", "De Haag"],
        "visits": 1,
    },
]


### Coding CHallenge 2 ###

# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.

travelLog = [
    {"country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]},
    {"country": "Germany", "visits": 5, "cities": ["Berlin", "Hamburg", "Stuttgart"]},
]


def addNewCountry(countryName, numVisits, citiesVisited):
    newDict = {}
    newDict["country"] = countryName
    newDict["visits"] = numVisits
    newDict["cities"] = citiesVisited
    travelLog.append(newDict)


addNewCountry("Netherlands", 1, ["Amsterdam", "Haarlem", "Rotterdam", "De Haag"])
print(travelLog)
