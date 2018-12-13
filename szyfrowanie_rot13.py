def rot5(z):
    if z > ord("4"):
        z -= 5
    else:
        z += 5

    return chr(z)


def rot13(z):
    if ord(chr(z).lower()) > ord("m"):
        z -= 13
    else:
        z += 13

    return chr(z)


def szyfruj(s):
    szyfr = ""

    for x in s:
        if x.isalpha():
            szyfr += rot13(ord(x))
        elif x.isdigit():
            szyfr += rot5(ord(x))
        else:
            szyfr += x

    return szyfr


while True:
    try:
        s = str(input())
        print(szyfruj(s))
    except EOFError:
        break
