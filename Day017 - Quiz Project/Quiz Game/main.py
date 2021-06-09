from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = []
for question in question_data:
    questionObject = Question(text = question["text"], answer = question["answer"])
    questionBank.append(questionObject)

quiz = QuizBrain(questionBank)

while quiz.stillHasQuestions():
    quiz.nextQuestion()
    
print("Quiz Completed")
print(f"\n\nYour final score was {quiz.score}/{quiz.questionNumber}")