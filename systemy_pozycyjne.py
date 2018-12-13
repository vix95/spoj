def dec2hex(d):
    return hex(d)[2:].upper()


def dec2eleven(d):
    l = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A"]
    x = int(d % 11)
    r = int(d / 11)
    if r == 0:
        return l[x]

    return dec2eleven(r) + l[x]


n = int(input())
for x in range(n):
    d = int(input())
    a, b = dec2hex(d), dec2eleven(d)
    print(str(a) + " " + str(b))
