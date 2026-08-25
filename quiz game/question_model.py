class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

question = Question(
    "Is Python a programming language?",
    "True"
)

print(question.text)
print(question.answer)