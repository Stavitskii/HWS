alfabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя "

def shift_encode(arg):
    str_list = []
    str_encode = ""
    for i in arg:
        str_list.append(i)
    for i in str_list:
        if i not in alfabet:
            str_encode += i
        elif i == "Я":
            str_encode += "А"
        elif i == "я":
            str_encode += "а"
        else:
            str_encode += alfabet[(alfabet.index(i)+1)]

    return str_encode

def shift_decode(arg):
    str_list = []
    str_encode = ""
    for i in arg:
        str_list.append(i)
    for i in str_list:
        if i not in alfabet:
            str_encode += i
        elif i == "А":
            str_encode += "Я"
        elif i == "а":
            str_encode += "я"
        else:
            str_encode += alfabet[(alfabet.index(i)-1)]

    return str_encode

print(shift_encode("Але! Я здеся. Хочу BMW, яхту и на Канары..."))
print(shift_decode("Бмё! А иеёта. Цпшф BMW, ацуф й об Лбобсь..."))

