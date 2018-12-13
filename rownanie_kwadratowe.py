def delta(a, b, c):
    d = b ** 2 - (4 * a * c)
    if d < 0:
        return 0
    elif d == 0:
        return 1
    else:
        return 2


for x in range(10):
    a, b, c = map(float, input().split())
    print(delta(a, b, c))
