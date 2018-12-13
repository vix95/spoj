def stringmerge(s1, s2):
    return ''.join(map(''.join, zip(s1, s2)))


n = int(input())
for x in range(0, n):
    s1, s2 = map(str, input().split())
    print(str(stringmerge(s1, s2)))
