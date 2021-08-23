'''
Too tired to read? 

Build a python script that takes a PDF file, identifies the text and converts the text to speech. 
Effectively creating a free audiobook.
'''

import gtts
from playsound import playsound
import pdfplumber

PDFfileURL = "/Users/brentlittlefield/Desktop/100DaysOfPython/Day087 - Projects Day 7 - PDF to Speech/test.pdf"
MP3fileURL = "/Users/brentlittlefield/Desktop/100DaysOfPython/Day087 - Projects Day 7 - PDF to Speech/test.mp3"

def main():
    pages = []
    allWords = ""
    with pdfplumber.open(PDFfileURL) as pdf:
        for i in range(0,len(pdf.pages)):
            pageobj = pdf.pages[i]
            pages.append(pageobj.extract_text().split("\n"))

    for page in pages:
        for sentence in page:
            for word in sentence.split(" "):
                allWords += f"{word} "
    sayWords(allWords)            

def sayWords(wordsToSay):
    tts = gtts.gTTS(wordsToSay)
    tts.save(MP3fileURL)
    playsound(MP3fileURL)

if __name__ == "__main__":
    main()