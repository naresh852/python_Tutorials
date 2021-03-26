from Question import question

question_prompts = [
    "what color are apples?\n(a)red\n(b)black\n(c)yellow\n\n",
    "what color are bananas?\n(a)teal\n(b)magenta\n(c)yellow\n\n",
    "what color are strawberries?\n(a)yellow\n(b)red\n(c)blue\n\n"
]
questions = [
    question(question_prompts[0],"a"),
    question(question_prompts[1],"c"),
    question(question_prompts[2],"b")
]
def test_run(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+=1
    print("you got "+str(score) +"/"+ str(len(questions))+" correct")

test_run(questions)