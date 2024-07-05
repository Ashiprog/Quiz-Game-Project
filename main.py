from data import question_data
from quiz_brain import QuizBrain


new_quiz = QuizBrain(question_data)
while new_quiz.still_has_questions():
    new_quiz.next_question()


print(f"You have completed the quiz. Your final score is {new_quiz.score}/{new_quiz.number}")