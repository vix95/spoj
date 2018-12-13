def palindrom(a):
    s, r = str(a), str(a)[::-1]
    counter = 0

    while s != r:
        s = str(int(s) + int(r))
        r = s[::-1]
        counter += 1

    print(str(s) + " " + str(counter))


n = int(input())
for x in range(0, n):
    a = int(input())
    palindrom(a)
