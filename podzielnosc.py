def podzielne(n, x, y):
    l = []
    for i in range(n):
        if i % x == 0 and i % y != 0:
            l.append(i)

    return l


t = int(input())
for i in range(t):
    n, x, y = map(int, input().split())
    l = podzielne(n, x, y)
    # ' '.join(l) nie dziala bo w liscie sa cyfry
    # trzeba przkeonwertowac na string
    s = ' '.join(str(j) for j in l)
    print(str(s))
