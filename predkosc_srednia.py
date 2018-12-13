def predkosc_srednia(a, b):
    return int(2 * a * b / (a + b))


n = int(input())
for x in range(n):
    a, b = map(int, input().split())
    print(str(predkosc_srednia(a, b)))
