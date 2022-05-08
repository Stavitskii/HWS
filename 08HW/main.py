import utils
import random

questions = utils.load_question()

random.shuffle(questions)


for question in questions:
    print(question.build_question())

    user_answer = input()
    question.user_answer = user_answer
    question.is_asked = True
    is_correct = question.is_correct()
    if is_correct:
        question.point = question.get_points()

    print(question.build_feedback())

utils.build_stats(questions)







