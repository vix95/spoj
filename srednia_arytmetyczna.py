def srednia(l):
    # pierwszy element niepotrzebny, ale zadanie wymaga
    # wiec kasujemy
    l.pop(0)
    avg = sum(l) / len(l)
    return min(l, key=lambda y: abs(y - avg))


n = int(input())
for x in range(n):
    l = list(map(int, input().split()))
    print(str(srednia(l)))
