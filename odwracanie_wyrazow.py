def odwroc(s):
    return s[::-1]


while True:
    try:
        s = input()
        print(odwroc(s))
    except EOFError:
        break
