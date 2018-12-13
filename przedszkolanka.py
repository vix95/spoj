def nwd(a, b):
    while b != 0:
        b, a = a % b, b

    return a


def nww(a, b):
    return abs(a * b / nwd(a, b))


n = int(input())
if n in range(0, 50):
    for x in range(0, n):
        a, b = map(int, input().split())
        print(int(nww(a, b)))
