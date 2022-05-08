import json

from classes.question import Question

def load_question():
    """
    Загружает вопросы из  файла JSON
    и возвращает в виде экземпляров класса Question
    """

    questions = []
    with open("data/questions.json", "r", encoding="utf-8") as file:
        question_raw = json.load(file)

    for question_raw in question_raw:
        q = question_raw.get("q")
        d = int(question_raw.get("d"))
        a = question_raw.get("a")
        new_question = Question(q, a, d)
        questions.append(new_question)

    return questions

def build_stats(questions):
    """
    Выводит статистику на основе списка вопросов
    """

    questions_correct_count = 0
    questions_points = 0
    for question in questions:
        if question.is_correct():
            questions_correct_count +=1
        questions_points += question.point

    print("Вот и всё!")
    print(f"Отвечено {questions_correct_count} вопроса из {len(questions)}")
    print(f"Набрано баллов: {questions_points}")


