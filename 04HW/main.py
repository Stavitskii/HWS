words_easy = {
    "family":"семья",
    "hand": "рука",
    "people":"люди",
    "evening": "вечер",
    "minute":"минута",
}

words_medium = {
    "believe":"верить",
    "feel": "чувствовать",
    "make":"делать",
    "open": "открывать",
    "think":"думать",
}

words_hard = {
    "rural":"деревенский",
    "fortune": "удача",
    "exercise":"упражнение",
    "suggest": "предлагать",
    "except":"кроме",
}

levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}

answers = {}
print("Выберите уровень сложности.\nЛегкий, средний, сложный.")
level = input().lower()

print(f"Выбран {level} уровень сложности. Мы предложим 5 слов, подберите перевод.\n")


if level == "легкий":
    words = words_easy

if level == "средний":
    words = words_medium

if level == "сложный":
    words = words_hard
for i in words:
    print(i, ",", len(words[i])," букв, начинается на ", words[i][0], ".")
    answer = input()
    if answer == words[i]:
        print(f"Верно. {i} - это {words[i]}\n")
        answers[i] = True
    else:
        print(f"Неверно. {i} - это {words[i]}\n")
        answers[i] = False
correct_answers = 0
if True in answers.values():
    print("Правильные слова")
    for i in answers:
        if answers[i]:
            print(i)
            correct_answers +=1
    print()


if False in answers.values():
    print("Неправильные слова")
    for i in answers:
        if not answers[i]:
            print(i)
    print()

print("Ваш ранг: ", levels[correct_answers])



