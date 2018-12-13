def wytnij(l):
    c = l[0]
    return print(l[1].replace(c, ""))


while True:
    try:
        l = list(map(str, input().split()))
        wytnij(l)
    except EOFError:
        break
