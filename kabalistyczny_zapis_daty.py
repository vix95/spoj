def zlicz(s):
    suma = 0
    for x in s:
        suma += dict[x.upper()]

    return print(suma)


dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'K': 10,
        'L': 20, 'M': 30, 'N': 40, 'O': 50, 'P': 60, 'Q': 70, 'R': 80, 'S': 90, 'T': 100,
        'V': 200, 'X': 300, 'Y': 400, 'Z': 500}
s = str(input())
zlicz(s)
