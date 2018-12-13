def sprawdz(l):
    if l[0] * l[2] <= l[1]:
        return "yes"
    else:
        return "no"


n = int(input())
for x in range(n):
    l = list(map(int, input().split()))
    print(sprawdz(l))
