def nwd(a, b):
    if a == 0 or b == 0:
        return 0
    while b != 0:
        a, b = b, a % b

    return a


n = int(input())
for x in range(0, n):
    a, b = map(int, input().split())
    print(str(nwd(a, b)))
