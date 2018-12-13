def ilosc_miejsc(n1, k1, n2, k2):
    return n1 * k1 + n2 * k2


n1, k1, n2, k2 = map(int, input().split())
print(str(ilosc_miejsc(n1, k1, n2, k2)))
