"""
Program summary

You will use what you've learnt to create a text-based (command line) program that takes any String input and converts it into Morse Code.
"""


translationDict = {
    'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', 
    
    ',':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', 
    '-':'-....-', '(':'-.--.', 
    ')':'-.--.-',
}

invertedDict = {
    value : key for (key, value) in translationDict.items()
}


# Given a plain string of text convert it to a morse encoding 
# any unsupported morse encodings will be replaced with an empty string
def encrypt(text):
    convertedText = ""
    for letter in text:
        if letter == " ":
            convertedText += "   "
        else:
            convertedText += f"{translationDict.get(letter,'')} "
    return convertedText[:-1]


# Given a string of morse text comprised of '.' and '-' in the format following will convert the text to english.
# 1. Each letter in morse is separated by one normal space " "
# 2. Each word in morse is separated by 3 normal spaces "   " 
# 3. Unsupported morse encodings will be subsitiuted by an empty string
def decrpty(text):
    plainText = ""
    for word in text.split("   "):
        for letter in word.split(" "):
            plainText += invertedDict.get(letter,'')
        plainText += " "
    return plainText


def main():
    textToConvert = input("Please enter the text you would like to convert to morse code: ").upper()
    
    morseText = encrypt(textToConvert)
    print(morseText)

    convertedBack = decrpty(morseText)
    print(convertedBack)
   

if __name__ == "__main__":
    main()