def porownaj(a, znak, b):
    if znak == "==":
        if a == b:
            return 1
        else:
            return 0
    elif znak == ">=":
        if a >= b:
            return 1
        else:
            return 0
    elif znak == "<=":
        if a <= b:
            return 1
        else:
            return 0
    elif znak == "!=":
        if a != b:
            return 1
        else:
            return 0


while True:
    try:
        l = list(map(str, input().split()))
        a = int(l.pop(0))
        znak = str(l.pop(0))
        b = int(l.pop(0))
        print(porownaj(a, znak, b))
    except EOFError:
        break
