from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=250,
            text="Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score = 0

        self.score_board = Label()
        self.score_board.config(text=f"Score: {self.score}", pady=20, bg=THEME_COLOR, fg="white")
        self.score_board.grid(row=0, column=1)

        false_image = PhotoImage(file="images/false.png")
        true_image = PhotoImage(file="images/true.png")

        self.btn_right = Button(image=true_image, command=self.true_pressed)
        self.btn_right.grid(row=2, column=0, pady=10)

        self.btn_wrong = Button(image=false_image, command=self.false_pressed)
        self.btn_wrong.grid(row=2, column=1, pady=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have reached the end of our Quiz\n your final score"
                                                            f"is: {self.score}/{self.quiz.question_number}")
            self.btn_wrong.config(state="disabled")
            self.btn_right.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
            self.score +=1
            self.score_board.config(text=f"Score: {self.score}")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.clear_screen)

    def clear_screen(self):
        self.canvas.config(bg="white")
        self.get_next_question()



