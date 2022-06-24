from data import question_data
from question_model import Question

question_bank = []
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    question = Question(q_text, q_answer)
    question_bank.append(question)

