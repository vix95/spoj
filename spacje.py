def formatString(l):
    for x in range(1, len(l)):
        if l[x - 1] == " ":
            l[x] = l[x].upper()

    return ''.join(l).replace(" ", "")


while True:
    try:
        l = list(input())
        print(formatString(l))
    except EOFError:
        break
