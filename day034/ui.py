from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.title("Quizzlers")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_lbl = Label(
            text="Score: 0",
            fg="white",
            bg=THEME_COLOR
        )
        self.score_lbl.grid(column=2, row=1, sticky="e")

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_txt = self.canvas.create_text(
            150, 
            125, 
            text="Loading...",
            width=280,
            fill=THEME_COLOR,
            font=("CiscoSans", 18, "normal")
        )
        self.canvas.grid(column=1, row=2, columnspan=2, pady=10, padx=10)

        self.true_btn = Button(text="True", command=self.true_btn_click)
        self.true_btn.grid(column=1, row=3)

        self.false_btn = Button(text="False", command=self.false_btn_click)
        self.false_btn.grid(column=2, row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.itemconfig(
            self.question_txt,
            text=self.quiz_brain.next_question()
        )

    def true_btn_click(self):
        pass

    def false_btn_click(self):
        pass