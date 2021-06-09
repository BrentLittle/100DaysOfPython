class QuizBrain:
    def __init__(self, qList):
        self.questionNumber = 0
        self.questionList = qList
        self.score = 0
    
    def nextQuestion(self):
        question = self.questionList[self.questionNumber]
        self.questionNumber += 1
        userAnswer = input(f"\nQ.{self.questionNumber}: {question.text} (True/False):")
        self.checkAnswer(userAnswer, question.answer)

    def stillHasQuestions(self):
        return self.questionNumber < len(self.questionList)

    def checkAnswer(self, userAnswer, correctAnswer):
        if userAnswer.lower() == correctAnswer.lower():
            print("That is Correct!")
            self.score += 1
        else:
            print("That is Incorrect!")
            print(f"The correct answer was {correctAnswer}.")
        print(f"Your current score is: {self.score}/{self.questionNumber}.")

