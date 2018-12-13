def zlicz_linie(s):
    return 1


rows = 0
while True:
    try:
        rows += zlicz_linie(input())
    except EOFError:
        print(rows)
        break
