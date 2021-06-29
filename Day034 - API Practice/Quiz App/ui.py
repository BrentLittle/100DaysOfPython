from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quizBrain:QuizBrain):
        self.quiz = quizBrain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.scoreLabel = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.scoreLabel.grid(row=0,column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.questionText = self.canvas.create_text(150,125, width=280, text="Some Question Text", fill=THEME_COLOR, font=("Arial",20,"italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        trueImage = PhotoImage(file="images/true.png")
        self.trueBtn = Button(image=trueImage, highlightthickness=0, command=self.truePressed)
        self.trueBtn.grid(row=2,column=0)

        falseImage = PhotoImage(file="images/false.png")
        self.falseBtn = Button(image=falseImage, highlightthickness=0, command=self.falsePressed)
        self.falseBtn.grid(row=2,column=1)

        self.getNextQuestion()

        self.window.mainloop()

    def getNextQuestion(self):

        self.canvas.config(bg="white")
        self.scoreLabel.config(text=f"Score: {self.quiz.score}")
        
        if self.quiz.still_has_questions():
            qText = self.quiz.next_question()
            self.canvas.itemconfig(self.questionText, text= qText)
        
        else:  
            self.canvas.itemconfig(self.questionText, text= f"You have reached the end of the quiz!\n\nYour final score was: {self.quiz.score}/10")
            self.trueBtn.config(state="disabled")
            self.falseBtn.config(state="disabled")


    def truePressed(self):
        self.provideFeedback(self.quiz.check_answer("True"))

    def falsePressed(self):
        self.provideFeedback(self.quiz.check_answer("False"))

    def provideFeedback(self, isRight):
        if isRight:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.getNextQuestion)