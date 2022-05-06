import json
from pprint import pprint as pp

def load_questions():
    """загружает вопросы из файла"""
    with open("questions.json", "r", encoding="utf-8") as file:
        questions = json.load(file)
    return questions

def show_field(questions):
    """выводит игровое поле"""
    top_level_cats = questions.keys()
    for top_cat in top_level_cats:
        print(top_cat.ljust(13), end="")
        cat_questions = questions[top_cat]
        for question_price, question_data in cat_questions.items():
            if question_data["asked"]:
                print(" ".ljust(7), end="")
            else:
                print(question_price.ljust(7), end="")
        print()

def parse_input(arg,questions):
    """делит ввод пользователя на категорию и число"""
    try:
        cat,price = arg.split()
    except:
        print("Неверный формат ввода")
        return False
    if not cat in questions.keys():
        print("Нет такой категории")
        return False
    if not price in questions[cat]:
        print("Нет такой стоимости вопроса")
        return False
    cat_from_questions = questions[cat]
    question_data = cat_from_questions[price]
    if question_data["asked"]:
        print("На этот вопрос уже отвечали")
        return False

    #return {"cat":cat, "price":int(price)}
    return cat, price

def show_question(cat,price,questions):
    """печатает вопрос"""
    result = questions[cat][price]["question"]
    return f"Слово {result} в переводе означает "

def show_stats(arg):
    """выводит статистику"""
    scores = arg["scores"]
    correct_answers = arg["correct_answers"]
    wrong_answers = arg["wrong_answers"]
    #scores = arg[0]
    #correct_answers = arg[1]
    #wrong_answers = arg[2]
    stats = f"Ваш счет: {scores}\nВерных ответов: {correct_answers}\nНеверных ответов: {wrong_answers}"
    return stats

def save_results_to_file(arg):
    """записывает результаты в JSON файл"""
    filename = "stats.json"
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(arg, file, ensure_ascii=False)

#questions = load_questions()


#print(show_field(questions))
#pp(show_field(questions))
#print(parse_input("Транспорт 100"))
#print(show_question(('Транспорт', "100")))
