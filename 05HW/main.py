from random import choice
morse = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}
words = ["code", "bit", "list", "soul", "next"]
answers=[]

def morse_encode(word):
    morse_word_list = []
    for i in word:
        morse_word_list.append(morse[i])
    morse_word = "".join(morse_word_list)
    return morse_word


def get_word():
  random_word = choice(words)
  return random_word

print("Сегодня мы потренируемся расшифровывать морзянку.\nНажмите Enter и начнем")
input()
while True:
  test_word = get_word()
  morse_word = morse_encode(test_word)
  answer = input(f"Слово {len(answers)+1} - {morse_word} ")
  if answer == "stop":
    break
  if answer == test_word:
    answers.append(True)
    print(f"Верно, {test_word}")
  else:
    print("Неверно")
    answers.append(False)


print(f"Всего задачек: {len(answers)}")
correct_answers=0
for i in answers:
  if i:
    correct_answers +=1
print(f"Отвечено верно: {correct_answers}")
print(f"Отвечено неверно: {len(answers) - correct_answers}")

