class QuizBrain:
    def __init__(self, q_list):
        self.number = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        current_question_set = self.q_list[self.number]
        current_question = current_question_set["text"]
        correct_answer = current_question_set["answer"]
        self.number += 1
        user_answer = input(f"Q{self.number} {current_question} True/False: ")
        self.check_answer(user_answer, correct_answer)

    def still_has_questions(self):
        return self.number < len(self.q_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Yay!! You got it right")
        else:
            print("You got it wrong.")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.number}")
        print("\n")

