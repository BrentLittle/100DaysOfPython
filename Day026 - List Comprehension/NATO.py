import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")


#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

alphabet = {row.letter: row.code for(index,row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

userInput = input("Enter a Word: ").upper()
output = [alphabet[letter] for letter in userInput]
print(output)