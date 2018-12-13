def licz(s):
    wynik = 0
    liczba = ""
    for x in s:
        if x.isdigit():
            liczba += x
        else:
            l.append(liczba)
            l.append(x)
            liczba = ""

    if liczba.isdigit():
        l.append(liczba)

    wynik = int(l.pop(0))
    while l:
        if l[0] == "+":
            l.pop(0)
            wynik += int(l.pop(0))
        elif l[0] == "-":
            l.pop(0)
            wynik -= int(l.pop(0))

    return wynik


l = []
n = int(input())
for x in range(n):
    s = str(input())
    print(licz(s))
