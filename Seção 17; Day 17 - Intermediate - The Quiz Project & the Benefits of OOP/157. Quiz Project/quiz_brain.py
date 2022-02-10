class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.user_score = 0
        self.question_list = questions_list

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answer(answer, question.answer)

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            print("You got it right!")
            self.user_score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {question_answer}.")
        print(f"Your current score is: {self.user_score}/{self.question_number}\n")
