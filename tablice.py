def odwroc(l):
    l.pop(0)
    return ' '.join(str(x) for x in list(reversed(l)))


n = int(input())
for x in range(0, n):
    l = list(map(int, input().split()))
    print(str(odwroc(l)))
