def carpet_string_ends(arg):
    result = ""
    length = range(arg)
    for i in length:
        if i == 0:
            result += "▓"
        elif i>0 and i<(len(length)-1):
            result+= "░"
        else:
            result+="▓"
    return result

def carpet_string(arg):
    result = ""
    length = range(arg)
    for i in length:
        if i == 0:
            result += "▓"
        elif i == 1 and len(length)>2:
            result += "░"
        elif i>1 and i<(len(length)-2):
            result+= "▒"
        elif i == (len(length)-2):
            result += "░"
        else:
            result+="▓"
    return result


def draw_carpet(w,h):
    lengs_h = len(range(h))
    result = ""
    for i in range(h):
        if i == 0:
            result += carpet_string_ends(w)
            result +="\n"
        elif i>0 and i<(lengs_h-1):
            result += carpet_string(w)
            result += "\n"
        else:
            result += carpet_string_ends(w)
    return result

print(draw_carpet(12,7))
