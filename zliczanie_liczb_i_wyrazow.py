def zlicz(l):
    liczby = 0
    wyrazy = 0

    for x in l:
        if x.isdigit():
            liczby += 1
        elif x.isalpha():
            wyrazy += 1

    return print(str(liczby) + " " + str(wyrazy))


while True:
    try:
        l = list(map(str, input().split()))
        zlicz(l)
    except EOFError:
        break
