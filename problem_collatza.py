def collatz(n):
    l.append(n)
    if n == 1:
        return

    if n % 2 == 0:
        collatz(n // 2)
    else:
        collatz(3 * n + 1)


n = int(input())
for x in range(0, n):
    l = []
    collatz(int(input()))
    print(str(len(l) - 1))
