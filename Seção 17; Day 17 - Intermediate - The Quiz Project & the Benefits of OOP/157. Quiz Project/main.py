from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question_dict in question_data:
    # Linha comentada para demonstrar a modularidade do código ao mudar apenas as chaves utilizadas no dicionário
    # question_bank.append(Question(question_dict["text"], question_dict["answer"]))
    question_bank.append(Question(question_dict["question"], question_dict["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed the quiz!\nYour final score was: {quiz.user_score}/{quiz.question_number}")
