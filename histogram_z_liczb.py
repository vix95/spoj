def tworz_histogram(l):
    maks = max(l)
    szerokosc = 30

    for x in range(-10, 11):
        gwiazdki = round(szerokosc * l[int(x) + 10] / maks)
        spacje = szerokosc - gwiazdki
        print('{: > 3}'.format(int(x)) + ":|" + "*" * gwiazdki + " " * spacje + "|")
    return


l = [0] * 21
while True:
    try:
        l[int(input()) - 11] += 1
    except EOFError:
        tworz_histogram(l)
        break
