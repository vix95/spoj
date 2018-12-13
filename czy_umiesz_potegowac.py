def potega(a, b, m):
    r = 1
    while b:
        if b & 1:
            r = r * a % m

        b >>= 1
        a *= a % m

    return r


D = int(input())
if D in range(0, 11):
    for x in range(0, D):
        a, b = map(int, input().split())
        print(str(potega(a, b, 10)))
