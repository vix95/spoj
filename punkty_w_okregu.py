def sprawdz(x, y, r, a, b):
    if (a - x) ** 2 + (b - y) ** 2 == r ** 2:
        return "E"
    elif (a - x) ** 2 + (b - y) ** 2 > r ** 2:
        return "O"
    else:
        return "I"


x, y, r = map(int, input().split())
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(sprawdz(x, y, r, a, b))
