def przesun(l, o):
    t = l
    for x in range(0, o):
        t = t[1:] + [t[0]]

    return ' '.join(t)


# zmienna n nie jest wykorzysytwana ale zadanie wymaga
n, o = map(int, input().split())
l = input().split(' ')
print(str(przesun(l, o)))
