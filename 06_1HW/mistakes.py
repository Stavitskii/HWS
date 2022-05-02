mistakes = {
  "out": "Вы вышли из системы ",
  "noaccess": "У вас нет доступа в этот раздел",
  "unknown": "Неизвестная ошибка",
  "timeout": "Система долго не отвечает",
  "robot": "Ваши действия похожи на робота",
}

def show_mistakes (*args):
    mistakes_list = []
    for i in args:
        if i in mistakes:
            mistakes_list.append(mistakes[i])
    return mistakes_list

print(show_mistakes("out", "robot", "unknown"))