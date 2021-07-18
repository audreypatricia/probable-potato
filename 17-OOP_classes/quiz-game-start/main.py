from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    question_bank.append(Question(data["text"], data["answer"]))

quiz = QuizBrain(question_bank)

quiz_running = True

while quiz_running:
    quiz.next_question()
    quiz_running = quiz.still_has_questions()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")