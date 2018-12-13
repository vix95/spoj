def push(l, a):
    l.append(a)
    return print(":)")


def pop(l):
    return print(str(l.pop(len(l) - 1)))


l = []
while True:
    try:
        c = input()
        if c == "+":
            a = input()
            if a.isdigit():
                a = int(a)
                if len(l) < 10:
                    push(l, a)
                else:
                    print(":(")
            else:
                print(":(")

        elif c == "-" and len(l) > 0:
            pop(l)
        else:
            print(":(")
    except EOFError:
        break
