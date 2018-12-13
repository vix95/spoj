def suma(a, sum):
    sum += a
    print(sum)
    return sum


sum = 0
for x in range(0, 10):
    a = int(input())
    sum = int(suma(a, sum))
