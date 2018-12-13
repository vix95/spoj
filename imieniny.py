def przydziel_cukierki(a, b):
    if a == 0 and b == 0:
        return print("NIE")
    elif a == 0 and b > 0:
        return print("TAK")
    elif a > b:
        return print("TAK")
    else:
        if a > b:
            if a % b == 0:
                return print("NIE")
            else:
                return print("TAK")
        else:
            if b % a == 0:
                return print("NIE")
            else:
                return print("TAK")


n = int(input())
for x in range(n):
    a, b = map(int, input().split())
    a -= 1  # odejmuje Jasia
    przydziel_cukierki(a, b)
