def suma(l):
    print(sum(l))
    return s.append(sum(l))


s = []
while True:
    try:
        l = list(map(int, input().split()))
        suma(l)
    except EOFError:
        print(sum(s))
        break
