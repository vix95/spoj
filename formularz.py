def sprawdz(l):
    imie = l[0][6:]
    nazwisko = l[1][11:]
    data_ur = l[2][11:]

    count = sprawdz_imie_nazwisko(imie)
    if count == 0:
        return 0

    count += sprawdz_imie_nazwisko(nazwisko)
    if count == 1:
        return 1

    count += sprawdz_data_ur(data_ur)
    return count


def ma_cyfry(s):
    for x in s:
        if x.isdigit():
            return 1

    return 0


def sprawdz_imie_nazwisko(s):
    if len(s) == 1:
        if s.isupper():
            return 1
        else:
            return 0
    else:
        if s[:1].isupper() and s[1:].islower() and not ma_cyfry(s) and s.isalpha():
            return 1
        else:
            return 0


def sprawdz_data_ur(s):
    if len(s) != 10:
        return 0

    l = list(s.split("-"))
    for x in range(len(l)):
        if l[x].isdigit():
            l[x] = int(l[x])
        else:
            return 0

    r = l[0]
    m = l[1]
    d = l[2]

    if r in range(1900, 2001) and m in range(1, 13) and d in range(1, 32):
        return 1
    else:
        return 0


while True:
    try:
        l = list(map(str, input().split(';')))
        print(sprawdz(l))
    except EOFError:
        break
