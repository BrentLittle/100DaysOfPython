# A testing program to be used for CISC101 assignment 3.
# It contains a main function that you cannot alter.  Your task is to complete
# this program by writing all the required functions.  Some functions will use
# default arguments. The testing code tests the use of default arguments first
# and then tests the functions without the use of any default arguments.

import random

def main() :
    random.seed()
    # Using default arguments wherever possible.  
    # Input files: word1.txt, word2.txt, word3.txt.  
    # 1000 insults generated, 
    # saved to file Insults.txt.
    
    # allWords is a tuple of three lists.
    allWords = loadInsults()
    print("One insult: ", end="")
    print(generateInsult(allWords))
    insults = generateInsults(allWords)
    displaySomeInsults(insults)
    saveInsults(insults)
    if checkInsultsFile() :
        print("\n1000 insults properly saved. They are unique and in order.")
    else :
        print("\nThe insults are not properly generated or saved!")

    # Using all possible arguments and prompting the user for the number of insults.
    allWords = loadInsults("word1.txt", "word2.txt", "word3.txt")
    numInsults = getNumInsults()
    insults = generateInsults(allWords, numInsults)
    displaySomeInsults(insults)
    saveInsults(insults, "Insults.txt")
    if checkInsultsFile(numInsults, "Insults.txt") :
        print("\n" + str(numInsults) + " insults properly saved. They are unique and in order.")
    else :
        print("\nThe insults are not properly generated or saved!")


# Write your functions here:
def loadInsults( file1Name = "word1.txt", file2Name = "word2.txt", file3Name = "word3.txt" ):
    file1 = open(file1Name,"r")
    file2 = open(file2Name,"r")
    file3 = open(file3Name,"r")

    file1Words = file1.readlines()
    file2Words = file2.readlines()
    file3Words = file3.readlines()
    
    for word in range(50):
        file1Words[word] = file1Words[word].strip("\n")
        file2Words[word] = file2Words[word].strip("\n")
        file3Words[word] = file3Words[word].strip("\n")
    
    file1.close()
    file2.close()
    file3.close()

    return (file1Words, file2Words, file3Words)

def generateInsult(wordTuple):
    w1 = random.choice(wordTuple[0])
    w2 = random.choice(wordTuple[1])
    w3 = random.choice(wordTuple[2])

    return f"Thou {w1} {w2} {w3}!"

def generateInsults( wordTuple, numInsults = 1000):
    listOfInsults = []

    for i in range(numInsults):
        newInsult = generateInsult(wordTuple)
        while newInsult in listOfInsults:
            newInsult = generateInsult(wordTuple)
        listOfInsults.append(newInsult)

    return listOfInsults

def displaySomeInsults(insults):
    first10 = insults[0:10]
    last10 = insults[-10:]

    for insult in first10:
        print(insult)
    for insult in last10:
        print(insult)

def saveInsults(insults, fileName = "Insults.txt"):
    insults.sort()
    output = open(fileName, 'w')
    
    for insult in insults:
        output.write(f"{insult}\n")
    
    output.close()

def checkInsultsFile( numInsults = 1000, fileName = "Insults.txt"):
    numInstultsInFile = 0
    
    insultFile = open(fileName, "r")
    insults = []
    
    for line in insultFile:
        insults.append(line)
        numInstultsInFile += 1
    
    sortedInsults = insults
    sortedInsults.sort()

    if (insults != sortedInsults) or (len(insults) != len(set(insults))) or (numInstultsInFile != numInsults):
        insultFile.close()
        return False
    else:
        insultFile.close()
        return True

def getNumInsults():
    return int(input("Enter Num Insults: "))

main()