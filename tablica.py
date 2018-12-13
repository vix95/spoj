# da rade zrobic za pomoca jednej linijki
# print(str(' '.join(input().split(' ')[::-1])))


def odwroc(l):
    return ' '.join(l[::-1])


l = input().split(' ')
print(str(odwroc(l)))
