def dwumian(n, k):
    r = 1
    for x in range(1, k + 1):
        r *= (n - x + 1) / x

    return round(r)


t = int(input())
for x in range(t):
    n, k = map(int, input().split())
    print(dwumian(n, k))
