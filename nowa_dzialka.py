def pole_kwadratu(a):
    return a ** 2


n = int(input())
for x in range(n):
    a = int(input())
    print(str(pole_kwadratu(a)))
