def polowa(s):
    return s[:int(len(s) / 2)]


n = int(input())
for x in range(n):
    s = input()
    print(str(polowa(s)))
