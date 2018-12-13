def silnia(n):
    if n == 0:
        return 1
    else:
        if n < 10:
            return silnia(n - 1) * n
        else:
            #return silnia(n - 1) * n
            return 0


D = int(input())
while D not in range(0, 31):
    D = int(input())

for x in range(0, D):
    n = int(input())
    while n not in range(0, 1000000001):
        n = int(input())

    if n in range(0, 1000000001):
        result = silnia(n)
        #print(result)
        print(str(int(result / 10) % 10) + " " + str(result % 10))
