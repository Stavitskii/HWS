alfabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя "

def check_pin(pin):
    """проверяет, является ли строка четырехбуквенным пин-кодом.
    Пин-код не может содержать 4 одинаковые цифры и быть равен 1234."""
    pin_list = []
    for i in pin:
        pin_list.append(i)
    pin_set = set(pin_list)

    if len(pin) !=4 or len(pin_set)==1 or not pin.isdigit() or pin == "1234":
        return False
    return True


def check_pass(password):
    """проверяет, чтобы пароль был не меньше 8 символов, содержал буквы и цифры."""
    password_list = []
    password_isdigit = ""
    password_isalfa = ""
    for i in password:
        password_list.append(i)
    if len(password)<8:
        return False
    for i in password_list:
        if i.isdigit():
            password_isdigit+=i
        if i.isalpha():
            password_isalfa+=i
    if len(password_isdigit)<1:
        return False
    if len(password_isalfa)<1:
        return False
    return True


def check_mail(mail):
    """проверяет наличие собачки и точки"""
    if not "@" in mail:
        return False
    elif not"." in mail:
        return False

    return True

def check_name(name):
    """проверяет содержание в имени только **русских** букв и пробелов."""
    for i in name:
        if i not in alfabet:
            return False
    return True

def check_all(pin=False, password=False, mail=False, name=False):
    """Проверяет все"""
    validate_dict = {}
    if not pin or not password or not mail or not name:
        print("Чего-то вы недоввели...")
        return None
    if check_pin(pin):
        validate_dict["pin"] = True
    else:
        validate_dict["pin"] = False

    if check_pass(password):
        validate_dict["password"] = True
    else:
        validate_dict["password"] = False

    if check_mail(mail):
        validate_dict["mail"] = True
    else:
        validate_dict["mail"] = False

    if check_name(name):
        validate_dict["name"] = True
    else:
        validate_dict["name"] = False

    if False in validate_dict.values():
        return False

    return True


