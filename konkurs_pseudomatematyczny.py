def wyniki(l):
    max_value = max(l)
    count_max = l.count(max_value)
    l.sort(reverse=True)
    t = []
    for x in range(count_max):
        t.append(max_value)
        l.pop(0)

    l.sort()
    return str(' '.join(map(str, t))) + " " + str(' '.join(map(str, l)))


n = int(input())
for x in range(n):
    a = int(input())  # nie wykorzystuje tego, zadanie wymaga
    l = list(map(int, input().split()))
    print(wyniki(l))
