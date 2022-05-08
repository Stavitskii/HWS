class Question:
    def __init__(self, text, answer, difficulty):
        """Принимает текст вопроса, правильный ответ, уровень сложности,
        создает из принятого признаки.
        Также создает признаки:
        - уже отвечали на вопрос, или нет
        - ответ пользователя на вопрос
        - набранные очки
        - максимальную сложность вопроса
        """
        self.text = text
        self.answer = answer
        self.difficulty = difficulty

        self.is_asked = False
        self.user_answer = None
        self.point = 0

        self.max_difficulty = 5

    def __repr__(self):
        return f" Сложность {self.difficulty}/{self.max_difficulty}, вопрос: {self.text}, ответ: {self.answer}"

    def get_points(self):
        """Возвращает int, количество баллов.
       Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
       """
        return self.difficulty *10

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответом, иначе False.
        """
        return self.answer == self.user_answer

    def build_question(self):
        """
        Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f"Вопрос: {self.text}\nСложность {self.difficulty}/{self.max_difficulty}"

    def build_feedback(self):
        """Возвращает :
        Ответ верный, получено __ баллов
        или
        Ответ неверный, верный ответ __
        """
        if self.is_correct():
            return f"Ответ верный, получено {self.get_points()} баллов.\n"
        return f"Ответ неверный, верный ответ {self.answer}.\n"



