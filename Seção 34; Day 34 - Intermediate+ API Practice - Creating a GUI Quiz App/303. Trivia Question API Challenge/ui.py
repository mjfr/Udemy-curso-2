import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tkinter.Label()
        self.score_label.config(text=f"Score: 0/{self.quiz.total_questions}", fg="white", font=("Segoe UI", 12, "bold"),
                                bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = tkinter.Canvas(bg="white", width=300, height=250, highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, text="Question goes here.", font=("Arial", 18, "italic"),
                                                     width=280)

        check_button_path = tkinter.PhotoImage(file="./images/true.png")
        x_button_path = tkinter.PhotoImage(file="./images/false.png")
        self.check_button = tkinter.Button()
        self.check_button.config(borderwidth=0, highlightthickness=0, image=check_button_path,
                                 command=self.check_pressed)
        self.check_button.grid(column=0, row=2)
        self.x_button = tkinter.Button()
        self.x_button.config(borderwidth=0, highlightthickness=0, image=x_button_path, command=self.x_pressed)
        self.x_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.check_button.config(state="active")
        self.x_button.config(state="active")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.total_questions}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.check_button.config(state="disabled")
            self.x_button.config(state="disabled")

    def check_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def x_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right is True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.check_button.config(state="disabled")
        self.x_button.config(state="disabled")
        self.window.after(1000, func=self.get_next_question)

