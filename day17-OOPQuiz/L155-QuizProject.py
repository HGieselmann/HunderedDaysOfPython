import question_data

class Question():
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuizBrain():
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions

    def serveQuestion(self):
        answer = input(f"Q.{self.question_number} {self.question_list[self.question_number].text} ")
        if answer == self.question_list[self.question_number].answer:
            print("Correct!")
            self.question_number += 1
            if self.questions_left(self.question_number):
                self.serveQuestion()
            else:
                print("Congratulations! You answered all questions correctly!")
        else:
            print(f"Sorry, wrong answer. You managed to answer {self.question_number} questions correctly. ")

    def questions_left(self, number):
        if number < len(self.question_list):
            return True
        else:
            return False





questions = []

for data in question_data.question_data:
    questions.append(Question(data["text"], data["answer"]))

quizBrain = QuizBrain(questions)
quizBrain.serveQuestion()







