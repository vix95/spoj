def konwertuj(s):
    flaga = False
    w = ""
    for c in s:
        if c == '>':
            flaga = False
        elif c == '<':
            flaga = True
        elif flaga:
            c = c.upper()
        w += c

    return w


while True:
    try:
        s = input()
        print(konwertuj(s))
    except EOFError:
        break
