def transpozycja(l):
    t = list(map(list, zip(*l)))
    for x in range(len(t)):
        print(str(' '.join(t[x])))

    return


l = []
# zmienna k nie jest wykorzystywana, zadanie wymaga
w, k = map(int, input().split())
for x in range(w):
    l.append(x)
    l[x] = list(input().split())

transpozycja(l)