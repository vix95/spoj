def wypisz(l, w):
    znak = w[0]
    liczba = int(w[1])

    for x in l:
        if znak == '>':
            if x > liczba:
                print(x)
        elif znak == '<':
            if x < liczba:
                print(x)

    return


l = []
n = int(input())
for x in range(n):
    l.append(int(input()))

w = list(map(str, input().split()))
wypisz(l, w)
