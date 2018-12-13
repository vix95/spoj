def reszta(a):
    if a % 15 == 0 and a >= 15:
        return "TAK"
    else:
        return "NIE"


while True:
    a = int(input())
    if a == 0:
        break
    print(reszta(a))
