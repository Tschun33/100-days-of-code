class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        q_text = current_question.text
        display_number = self.question_number + 1
        choice = input(f"Q{display_number}. {q_text}. Is it True or False?")
        if choice == current_question.answer:
            self.question_number += 1
            print("You are right!")
            return True
        else:
            print(f"Wrong answer! Your score is: {self.question_number} ")
            return False

