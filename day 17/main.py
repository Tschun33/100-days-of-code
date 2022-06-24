from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
is_right = True
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    question = Question(q_text, q_answer)
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)

while is_right:
    is_right = quiz_brain.next_question()
