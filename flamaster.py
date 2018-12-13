def f(l):
    a = []
    counter = 1
    for x in range(1, len(l) + 1):
        if counter == 1:
            a.append(l[x - 1])

        if x < len(l):
            if l[x - 1] == l[x]:
                counter += 1
            elif counter == 2:
                a.append(l[x - 1])
                counter = 1
            elif counter != 1:
                a.append(counter)
                counter = 1
        elif counter > 2:
            a.append(counter)
        elif counter == 2:
            a.append(l[x - 1])

    return a


n = int(input())
if n in range(0, 50):
    for x in range(0, n):
        l = list(input())
        #l = "ABBCCCDDDDEEEEEFGGHIIJKKKL"
        #l = "AAAAAAAAAABBBBBBBBBBBBBBBB"
        #l = "SSFFSAAAEE"
        #l = "AAAAAAAAAAAFFFFFFFFFFFFFFEEF"
        s = ''.join(str(x) for x in f(l))
        print(s)
