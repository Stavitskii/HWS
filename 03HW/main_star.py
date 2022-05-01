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
    attempts = 3
    for i in range(attempts):
        answer = input(f"{question}\n")
        if answer == answers[count]:
            scores += 10 - ((3-attempts)*2)
            print("Ответ верный!\n" + f"Вы получаете {10 - ((3-attempts)*2)} баллов\n")
            break
        else:
            attempts -= 1
            if attempts == 0:
                print("К сожалению попыток больше не осталось\n")
                break
            else:
                print(f"Ответ неверный, осталось {attempts} попыток.")
                continue
    count +=1


print(f"Вот и все!")
print(f"Вы ответили на {count} вопросов, из них на {int(scores/10)} верно.")
print(f"Вы заработали {scores} балов.")
print(f"Это {round(100/30*scores)} процентов.")
