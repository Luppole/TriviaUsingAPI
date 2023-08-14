from question_model import Question
from data import questions
from quiz_brain import QuizBrain
from ui import QuizUI

question_bank = []
for question in questions:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
ui = QuizUI(quiz)

while quiz.still_has_questions():
    quiz.next_question()
