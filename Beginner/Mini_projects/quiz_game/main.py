from question_with_answer import QuestionWithAnswer

questions = [
    "What is the currency name of Bangladesh? \n (a) Dollar\n (b) Euro\n (c) Taka",
    "What is the capital of Bangladesh? \n (a) Dhaka\n (b) Moscow\n (c) London",
    "What is the national fruit of Bangladesh? \n (a) Mango\n (b) Licchi\n (c) Jackfruit",
    "What is the national fish of Bangladesh? \n (a) Ruhi\n (b) Hilsha\n (c) Salmon",
    "What is the national animal of Bangladesh? \n (a) Lion\n (b) Tiger\n (c) Python"
]


quiz = [
    QuestionWithAnswer(questions[0], "c"),
    QuestionWithAnswer(questions[1], "a"),
    QuestionWithAnswer(questions[2], "c"),
    QuestionWithAnswer(questions[3], "b"),
    QuestionWithAnswer(questions[4], "b")
]

def start_quiz(quiz):
    score = 0
    
    for qz in quiz:
        answer = input(qz.question + "\nEnter your answer: ")

        if answer == qz.answer:
            score += 1

    print("\nYour score " + str(score) + "/" + str(len(quiz)))
    

start_quiz(quiz)
        
