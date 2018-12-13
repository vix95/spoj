def zlicz(l):
    poszukiwana = l.pop(0)
    n = l.pop(0)  # nie korzystam z tego, zadanie wymaga
    return l.count(poszukiwana)


while True:
    try:
        l = list(map(int, input().split()))
        print(str(zlicz(l)))
    except EOFError:
        break
