from ui import QuizInterface
from question_model import Question
from quiz_brain import QuizBrain
import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}


r = requests.get(url="https://opentdb.com/api.php", params=parameters)
r.raise_for_status()
question_data = r.json()["results"]
print(r)


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
ui = QuizInterface(quiz)
# while quiz.still_has_questions():
#     quiz.next_question()
