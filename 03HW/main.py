print("Привет! Предлагаю проверить свои знания английского!\n"+'Наберите "ready" чтобы начать.')
ready = input()
if ready != "ready":
    print("Кажется, вы не хотите играть. Очень жаль")
    quit()

questions = ["My name ___Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]
count = 0
scores = 0

for question in questions:
    answer = input(f"{question}\n")
    if answer == answers[count]:
        scores += 10
        print("Ответ верный!\n" + "Вы получаете 10 баллов\n")
    else:
        print("Ответ неверный\n" + f"Правильный ответ {answers[count]}\n")
    count +=1


print(f"Вот и все!")
print(f"Вы ответили на {count} вопросов, из них на {int(scores/10)} верно.")
print(f"Вы заработали {scores} балов.")
print(f"Это {round(100/30*scores)} процентов.")

