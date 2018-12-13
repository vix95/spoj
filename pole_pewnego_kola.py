def pole(r, d):
    return (r ** 2 - (d ** 2 / 4)) * pi


pi = 3.141592654
r, d = map(float, input().split())
print(str("%.2f" % pole(r, d)))
