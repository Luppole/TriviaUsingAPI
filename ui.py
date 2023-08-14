from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"

class QuizUI:

    def __init__(self, quizBrain: QuizBrain):
        self.quiz = quizBrain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(fg="white", bg=THEME_COLOR, text=f"Score: {quizBrain.score}")
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=270, bg="white")
        self.text = self.canvas.create_text(150, 125, text=quizBrain.current_question, fill=THEME_COLOR, font=("Ariel", 20, "italic"), width=300)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50, padx=40)
        trueImage = PhotoImage(file="images/true.png")
        falseImage = PhotoImage(file="images/false.png")

        self.trueButton = Button(image=trueImage, highlightthickness=0, command=self.AnswerTrue)
        self.falseButton = Button(image=falseImage, highlightthickness=0, command=self.AnswerFalse)
        self.answer = ""

        self.trueButton.grid(row=2, column=0)
        self.falseButton.grid(row=2, column=1)

        self.GenerateText()

        self.window.mainloop() 
    
    def GenerateText(self):
        self.score.config(text=f"Score: {self.quiz.score}")
        question = self.quiz.next_question()
        self.canvas.itemconfig(self.text, text=question)
    
    def AnswerTrue(self):
        isRight = self.quiz.check_answer("True")
        self.Feedback(isRight)
    
    def AnswerFalse(self):
        isRight = self.quiz.check_answer("False")
        self.Feedback(isRight)

    def Feedback(self, isRight):
        if(isRight == True):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000, self.GenerateText())









