def cezar(s, offset):
    s2 = ""
    for c in s:
        if c.isalpha():
            z = ord(c) + offset
            if z > ord("Z"):
                z -= 26

            s2 += chr(z)
        else:
            s2 += " "

    return s2


while True:
    try:
        s = input()
        print(cezar(s, 3))
    except EOFError:
        break
