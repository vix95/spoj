def rozbij(c):
    # utf-8
    b = bin(c)[2:]
    b1 = b[:-6]
    b2 = b[-6:]

    while len(b1) != 6:
        b1 = "0" + b1

    while len(b2) != 7:
        b2 = "0" + b2

    b1 = "11" + b1
    b2 = "1" + b2

    #print("bin: " + str(b) + "(" + str(int(b, 2)) + ") b1: " + str(b1) +
    #      " (" + str(int(b1, 2)) + ") b2: " + str(b2) + "(" + str(int(b2, 2)) + ")")

    l[int(b1, 2)] += 1
    l[int(b2, 2)] += 1

    return


def zlicz(s):
    l[10] += 1  # new line
    for x in s:
        if ord(x) > 128:
            rozbij(ord(x))
        else:
            l[ord(x)] += 1

    return


l = [0] * 255
while True:
    try:
        s = str(input())
        zlicz(s)
    except EOFError:
        for x in range(len(l)):
            if l[x] != 0:
                print(str(x) + " " + str(l[x]))

        break
