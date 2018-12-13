def dodawanie(a, b):
    return a + b


def odejmowanie(a, b):
    return a - b


def mnozenie(a, b):
    return a * b


def dzielenie(a, b):
    if b == 0:
        return 0
    else:
        return int(a / b)


def modulo(a, b):
    return a % b


while True:
    try:
        d, a, b = input().split()
        a, b = int(a), int(b)
        if d == "+":
            print(str(dodawanie(a, b)))
        elif d == "-":
            print(str(odejmowanie(a, b)))
        elif d == "*":
            print(str(mnozenie(a, b)))
        elif d == "/":
            print(str(dzielenie(a, b)))
        elif d == "%":
            print(str(modulo(a, b)))
    except EOFError:
        break
