def przesun(l):
    l.pop(0)
    return ' '.join(l[1:] + [l[0]])


n = int(input())
for x in range(0, n):
    a = input()
    l = a.split(' ')
    print(str(przesun(l)))
