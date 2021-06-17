## List Comprehension
# create a new list from an already created list

# NameOfNewList = [newItem for item in list]

numbers = [1, 2, 3]
print(numbers)

newList = [num + 1 for num in numbers]
print(newList)

name = "Brent"
print(name)
newName = [letter for letter in name]
print(newName)

rangeList = [2*index for index in range(1,5)]
print(rangeList)

names = ["Brent","Sheldon","Kelston","Dwayne","Erik"]
shortNames = [name for name in names if len(name) < 6]
print(shortNames)

upperLongNames = [name.upper() for name in names if len(name)>=6]
print(upperLongNames)


### Exercise 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squaredNums = [num**2 for num in numbers]
print(squaredNums)


### Exercise 2
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
evenNums = [num for num in numbers if num%2==0]
print(evenNums)


### Exercise 3
list1 = [3, 6, 5, 8, 33, 12, 7, 4, 72, 2, 42, 13]
list2 = [3, 6, 13, 5, 7, 89, 12, 3, 33, 34, 1, 344, 42]
result = [num for num in list1 if num in list2]
print(result)



### Dictionary Comprehension
# newDict = {newKey:newVal for item in list}
# OR
# newDict = {newKey:newVal for (key,value) in dict.items() if test}
import random

names = ["Brent","Sheldon","Kelston","Dwayne","Erik"]
studentScores = {studentName:random.randint(0,100) for studentName in names}
print(studentScores)

passedStudents = {key:value for (key,value) in studentScores.items() if value>=50}
print(passedStudents)


## Exercise 4
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
wordDict = {word:len(word) for word in sentence.split()}
print(wordDict)


## Exercise 5
weatherC = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weatherF = {key:(value * 9/5) + 32 for (key,value) in weatherC.items()}
print(weatherF)


