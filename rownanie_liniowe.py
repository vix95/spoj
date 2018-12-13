def rownanie_liniowe(a, b, c):
    # ax + b = c
    if b == c:
        return print("NWR")
    elif a == 0:
        return print("BR")
    else:
        print("%.2f" % round((c - b) / a, 2))


a, b, c = map(float, input().split())
rownanie_liniowe(a, b, c)
