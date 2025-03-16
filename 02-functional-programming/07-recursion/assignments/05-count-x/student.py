def countX(text):
    if len(text) == 1:
        return 1 if text[0] == "x" else 0
    elif len(text) == 0:
        return 0
    else:
        value = 1 if text[0] == "x" else 0
        return value + countX(text[1:])