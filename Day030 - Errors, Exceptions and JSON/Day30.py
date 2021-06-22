# with open("text.txt") as file:
#     file.read()

# Key Errors from Dictionaries
# IndexError for indexing lists or other iterables
# Type Error


"""
Try: Something that might cause an exception

Except: Do this if there WAS an exception

Else: Do this if there WAS NOT an exception

finally: Do this no matter what happens without respect to error catched or not
"""
try:
    file = open("aFile.txt")
    dictionary = {"Key":"Value"}
    print(dictionary["Key"])
except FileNotFoundError:
    file = open("aFile.txt","w")
    file.write("something")
except KeyError as msg:
    print(f"Key {msg} Not Found")
else:
    content = file.read()
    print(content)
finally:
    #raise KeyError
    file.close()
    print("file Closed")





height = float(input("Height (meters): "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 Meters")

bmi = weight/(height**2)
print(bmi)


## Code Exercise 
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet = {row.letter: row.code for(index,row) in data.iterrows()}

def generateMapping():
    userInput = input("Enter a Word: ").upper()
    try:
        output = [alphabet[letter] for letter in userInput]
    except KeyError:
        print("Sorry, Please only enter characters from the alphabet")
        generateMapping()
    else:
        print(output)

generateMapping()




## Working with JSON
# we can use the inbuilt JSON library to a JSON file
