def licz(l):
    pion = l[0] - l[1]
    poziom = l[2] - l[3]

    if pion == 0 and poziom == 0:
        return print("studnia")

    if pion > 0:
        print(str(0) + " " + str(pion))
    elif pion < 0:
        print(str(1) + " " + str(abs(pion)))

    if poziom > 0:
        print(str(2) + " " + str(poziom))
    elif poziom < 0:
        print(str(3) + " " + str(abs(poziom)))


d = int(input())
for x in range(0, d):
    l = [0, 0, 0, 0]  # 0 - polnoc, 1 - poludnie, 2 - zachod, 3 - wschod
    n = int(input())
    for y in range(0, n):
        a, b = map(int, input().split())
        l[a] += b

    licz(l)
