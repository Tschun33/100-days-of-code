from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
is_right = True
has_questions = True
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    question = Question(q_text, q_answer)
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)

while has_questions:
    quiz_brain.next_question()
    has_questions = quiz_brain.still_has_questions()

print("Congratulations. You completed the quiz")
print(f"Your final score is: {quiz_brain.score}/{len(question_bank)}")
