import utils

questions = utils.load_questions()
scores = 0
correct_answers = 0
wrong_answers = 0

while True:
    q_list = []
    for i in questions.values():
        for q in i.values():
            q_list.append(q['asked'])
            q_set = set(q_list)


    if q_set == {True}:
        break

    utils.show_field(questions)
    user_input = input("Выберите категорию и вопрос ")
    if user_input == "Стоп":
        break
    if utils.parse_input(user_input, questions):
        cat, price = utils.parse_input(user_input, questions)
        print(utils.show_question(cat,price,questions))
    else:
        continue
    user_answer = input()

    if user_answer == questions[cat][price]["answer"]:
        scores += int(price)
        correct_answers += 1
        print(f"Верно, +{price}. Ваш счет =  {scores}")
        questions[cat][price]["asked"]=True
    else:
        scores -= int(price)
        wrong_answers += 1
        print(f"Неверно, на самом деле {questions[cat][price]['answer']}. Ваш счет = {scores}")
        questions[cat][price]["asked"] = True

print("У нас закончились вопросы")
statistics = {"scores":scores, "correct_answers":correct_answers, "wrong_answers":wrong_answers}
print(utils.show_stats(statistics))
utils.save_results_to_file(statistics)
