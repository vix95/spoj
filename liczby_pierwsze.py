def liczba_pierwsza(n):
    if n < 2:
        return print("NIE")

    for x in range(2, n):
        if n % x == 0:
            return print("NIE")

    return print("TAK")


n = int(input())
if n > 0 and n < 100000:
    for x in range(0, n):
        a = int(input())
        liczba_pierwsza(a)
