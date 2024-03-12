import tkinter as tk

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("QUIZ")
        self.master.geometry('1500x900')
        self.score = 0
        self.question_number = 0
        self.questions = [
            {"question": "Which of them is a Keyword in Python?", "options": ["range", "def", "Val", "to"], "answer": "def"},
            {"question": "Which of the following is built-in function in Python?", "options": ["factorial()", "print()", "seed()", "sqrt()"], "answer": "print()"},
            {"question": "Which of the following is not the core datatype in Python?", "options": ["Tuple", "Dictionary", "Lists", "Class"], "answer": "Class"},
            {"question": "Who developed python programming language?", "options": ["Wick Van Rossum", "Rasmus Lerdorf", "Guido Van Rossum", "Niene Stom"], "answer": "Guido Van Rossum"},
            {"question": "Which of the following is the extension for Python File?", "options": [".python", ".p", ".pl", ".py"], "answer": ".py"},
            {"question": "Which of the following data types is immutable in Python?", "options": ["List", "Tuple", "Dictionary", "Set"], "answer": "Tuple"},
            {"question": "What is the output of '2' + '3' in Python?", "options": ["5", "23", "Error", "None"], "answer": "23"},
            {"question": "What is the correct way to declare a variable in Python?", "options": ["variable x;", "x = 10;", "int x = 10;", "None of the above"], "answer": "x = 10;"},
            {"question": "What does the 'range()' function in Python return?", "options": ["A list of numbers", "A generator object", "A dictionary", "A tuple"], "answer": "A generator object"},
            {"question": "Which method is used to remove duplicates from a list in Python?", "options": ["unique()", "distinct()", "remove_duplicates()", "set()"], "answer": "set()"}
        ]
        
        self.label_t = tk.Label(master, text="QUIZ", font=("arial", 50))
        self.label_t.place(x=600, y=50)

        self.label_u = tk.Label(master, text="Username", font=("arial", 30))
        self.label_u.place(x=250, y=250)

        self.entry = tk.Entry(master, font=("arial", 30))
        self.entry.place(x=500, y=250)

        self.button0 = tk.Button(master, text="ENTER", font=("arial", 30), command=self.display_question)
        self.button0.place(x=600, y=350)

        self.close_button = tk.Button(master, text="CLOSE", font=("arial", 20), bg="red", fg="white", command=self.close_app)
        self.close_button.place(x=100, y=800)

    def display_question(self):
        self.username = self.entry.get()
        self.label_u.destroy()
        self.entry.destroy()
        self.button0.destroy()
        self.show_next_question()

    def show_next_question(self):
        if self.question_number < len(self.questions):
            question_data = self.questions[self.question_number]
            self.label_q = tk.Label(self.master, text=f"Question {self.question_number + 1}", font=("Arial", 35))
            self.label_q.place(x=550, y=50)

            self.label_question = tk.Label(self.master, text=question_data["question"], font=("Arial", 30))
            self.label_question.place(x=300, y=100)

            self.buttons = []
            for idx, option in enumerate(question_data["options"]):
                button = tk.Button(self.master, text=option, font=("Arial", 20), command=lambda idx=idx: self.check_answer(idx))
                button.place(x=400 if idx < 2 else 800, y=200 + 100 * (idx % 2))
                self.buttons.append(button)
        else:
            self.display_score()

    def check_answer(self, idx):
        selected_option = self.questions[self.question_number]["options"][idx]
        correct_answer = self.questions[self.question_number]["answer"]
        if selected_option == correct_answer:
            self.score += 1
        self.question_number += 1
        self.clear_question()

    def clear_question(self):
        self.label_q.destroy()
        self.label_question.destroy()
        for button in self.buttons:
            button.destroy()
        self.show_next_question()

    def display_score(self):
        self.label_score = tk.Label(self.master, text=f"SCORE: {self.score}", font=("Arial", 30))
        self.label_score.place(x=400, y=300)
        self.label_username = tk.Label(self.master, text=f"Username: {self.username}", font=("Arial", 30))
        self.label_username.place(x=400, y=200)
        

    def retake_quiz(self):
        self.score = 0
        self.question_number = 0
        self.label_score.destroy()
        self.label_username.destroy()
        self.retake_button.destroy()
        self.display_question()

    def close_app(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
