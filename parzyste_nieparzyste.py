def parzyste_nieparzyste(l):
    # zadanie wymaga wczytac pierwsza liczbe, ktorej nie potrzebuje
    # bo i tak uzywam listy
    l.pop(0)
    parzyste = []
    nieparzyste = []

    # parzyste
    for x in range(len(l)):
        if (x + 1) % 2 == 0:
            parzyste.append(l[x])

    # nieparzyste
    for x in range(len(l)):
        if (x + 1) % 2 != 0:
            nieparzyste.append(l[x])

    return print(str(' '.join(parzyste)) + " " + str(' '.join(nieparzyste)))


n = int(input())
for x in range(n):
    l = list(input().split())
    parzyste_nieparzyste(l)
