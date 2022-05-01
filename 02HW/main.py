print("Привет! Предлагаю проверить свои знания английского!\n"+"Расскажи, как тебя зовут!")
user_name = input()

print(f"Привет, {user_name}, начинаем тренировку")

scores = 0
name = input(f"My name ___ {user_name}\n")
if name == "is":
    scores += 10
    print("Ответ верный!\n"+"Вы получаете 10 баллов\n")
else:
    print("Ответ неверный\n"+"Правильный ответ is\n")

ocupation = input("I___a coder\n")
if ocupation == "am":
    scores += 10
    print("Ответ верный!\n"+"Вы получаете 10 баллов\n")
else:
    print("Ответ неверный\n"+"Правильный ответ am\n")

live = input("I live___Moscow\n")
if live == "in":
    scores += 10
    print("Ответ верный!\n"+"Вы получаете 10 баллов\n")
else:
    print("Ответ неверный\n"+"Правильный ответ in\n")

print(f"Вот и все, {user_name}!")
print(f"Вы ответили на {int(scores/10)} вопросов верно.")
print(f"Вы заработали {scores} балов.")
print(f"Это {round(100/30*scores)} процентов.")
