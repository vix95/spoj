def licz(l):
    l.pop(0)  # nie korzystam z tego, zadanie wymaga
    return sum(l) + len(l) - 1


n = int(input())
for x in range(n):
    l = list(map(int, input().split()))
    print(licz(l))
