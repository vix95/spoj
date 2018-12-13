def przelicz_na_ciastka(w):
    return int(86400 / w)


t = int(input())
for x in range(0, t):
    suma = 0
    n, m = map(int, input().split())
    for y in range(0, n):
        s = int(input())
        suma += przelicz_na_ciastka(s)

    print(str(int(suma / m) + (suma % m > 0)))
