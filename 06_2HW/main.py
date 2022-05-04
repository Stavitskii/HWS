import random

name = input("Введите ваше имя \n")

scores = 0
with open("words.txt", "r", encoding="UTF-8") as file:
    words = file.read()
words_list = words.split()

for i in words_list:
    i_list = []
    for letter in i:
        i_list.append(letter)
        random.shuffle(i_list)
    shuffle_word = "".join(i_list)
    answer = input(f"Угадайте слово {shuffle_word} ")
    if answer == i:
        scores += 10
        print("Верно! Вы получаете 10 очков")
    else:
        print(f"Неверно! Верный ответ - {i}")
result = f"{name} {scores}"

with open("results.txt", "a", encoding="UTF-8") as file:
    file.write(f"{result}\n")

with open("results.txt") as file:
    count_games=0
    record=0
    for line in file:
        count_games += 1
        line_list = line.split()
        if int(line_list[1])>record:
            record = int(line_list[1])
print(f"Всего сыграно игр: {count_games}\nМаксимальный рекорд: {record}")









