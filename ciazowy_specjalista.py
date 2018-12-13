def wzor(x, y, z):
    return round((z * y - (x + y)) / (z - 1) * 12)


n = int(input())
for i in range(n):
    x, y, z = map(int, input().split())
    print(wzor(x, y, z))
