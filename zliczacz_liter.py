def zlicz_znaki(l):
    # [[x, l.count(x)] for x in set(l)]
    tLowerCount = [l.count(x) for x in set(l) if x.islower()]
    tUpperCount = [l.count(x) for x in set(l) if x.isupper()]
    tLower = [x for x in set(l) if x.islower()]
    tUpper = [x for x in set(l) if x.isupper()]
    tL = list(zip(tLower, tLowerCount))
    tU = list(zip(tUpper, tUpperCount))
    tL = sorted(tL, key=lambda x: x[0])
    tU = sorted(tU, key=lambda x: x[0])

    # male
    for x in range(len(tL)):
        print(str(tL[x][0]) + " " + str(tL[x][1]))

    # duze
    for x in range(len(tU)):
        print(str(tU[x][0]) + " " + str(tU[x][1]))


s = ""
n = int(input())
for x in range(n):
    s += input()

l = [x for x in s.replace(" ", "")]
zlicz_znaki(l)
