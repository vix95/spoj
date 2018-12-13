def suma(l):
    s = 0
    for x in l:
        s += int(x)

    return s


t = int(input())
for x in range(0, t):
    n = int(input())  # to i tak nic nie robi ale zadanie wymaga
    a = input()
    l = a.split(' ')
    print(str(suma(l)))
