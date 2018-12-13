def dodawanie(a, b, l):
    return l[a] + l[b]


def odejmowanie(a, b, l):
    return l[a] - l[b]


def mnozenie(a, b, l):
    return l[a] * l[b]


def dzielenie(a, b, l):
    if l[b] == 0:
        return 0
    else:
        return int(l[a] / l[b])


def modulo(a, b, l):
    return l[a] % l[b]


def pamiec(a, b, l):
    l[a] = b
    return l


l = [0] * 10
while True:
    try:
        d, a, b = input().split()
        a, b = int(a), int(b)
        if d == "+":
            print(str(dodawanie(a, b, l)))
        elif d == "-":
            print(str(odejmowanie(a, b, l)))
        elif d == "*":
            print(str(mnozenie(a, b, l)))
        elif d == "/":
            print(str(dzielenie(a, b, l)))
        elif d == "%":
            print(str(modulo(a, b, l)))
        elif d == "z":
            pamiec(a, b, l)
    except EOFError:
        break
