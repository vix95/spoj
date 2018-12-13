def pesel(l):
    suma = int(l[0]) * 1 + int(l[1]) * 3 + \
           int(l[2]) * 7 + int(l[3]) * 9 + \
           int(l[4]) * 1 + int(l[5]) * 3 + \
           int(l[6]) * 7 + int(l[7]) * 9 + \
           int(l[8]) * 1 + int(l[9]) * 3 + \
           int(l[10]) * 1

    if suma > 0 and suma % 10 == 0:
        return "D"
    else:
        return "N"


n = int(input())
for x in range(0, n):
    l = list(input())
    print(str(pesel(l)))
