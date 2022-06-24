class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        q_text = current_question.text
        display_number = self.question_number + 1
        self.question_number += 1
        choice = input(f"Q{display_number}. {q_text}. Is it True or False?")
        self.check_answer(choice, current_question)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, choice, c_question):
        if choice.lower() == c_question.answer.lower():
            self.score += 1
            print("You are right!")
        else:
            print("Your are wrong")
        print(f"Your score is:{self.score}/{self.question_number}")



