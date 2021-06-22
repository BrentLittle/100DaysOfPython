from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"
currentWord = {}
words = {}


try:
    data = pandas.read_csv("data/wordsToLearn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    words = data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")



def nextCard():
    global currentWord, flipTimer
    window.after_cancel(flipTimer)
    currentWord = random.choice(words)
    canvas.itemconfig(cardTitle, text="French", fill="black")
    canvas.itemconfig(cardWord, text=currentWord["French"], fill="black")
    canvas.itemconfig(cardFace, image=frontImg)
    window.after(3000, func=flipCard)
    
def flipCard():
    canvas.itemconfig(cardTitle, text="English", fill="white")
    canvas.itemconfig(cardWord, text=currentWord["English"], fill="white")
    canvas.itemconfig(cardFace, image=backImg)

def isLearnt():
    words.remove(currentWord)
    data = pandas.DataFrame(words)
    data.to_csv("data/wordsToLearn.csv", index=False)
    nextCard()

window = Tk()
window.title("Flash Card French - English")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flipTimer = window.after(3000, func=flipCard)

canvas    = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
frontImg  = PhotoImage(file="images\card_front.png")
backImg   = PhotoImage(file="images\card_back.png")
cardFace  = canvas.create_image(400, 263, image=frontImg)
cardTitle = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
cardWord  = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

unknownImg = PhotoImage(file="images\wrong.png")
unknownBtn = Button(image=unknownImg, highlightthickness=0, command=nextCard)
unknownBtn.grid(row=1,column=0)

checkImg = PhotoImage(file="images/right.png")
checkBtn = Button(image=checkImg, highlightthickness=0, command=isLearnt)
checkBtn.grid(row=1,column=1)


nextCard()
window.mainloop()