def nierownosc(a, b, c):
    if (a > 0) and (b > 0) and (c > 0) and (a + b > c) and (a + c > b) and (b + c > a):
        return 1
    else:
        return 0


while True:
    try:
        a, b, c = map(float, input().split())
        print(str(nierownosc(a, b, c)))
    except EOFError:
        break
