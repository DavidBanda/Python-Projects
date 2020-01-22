array = [1, 3, 5, 7, 9, 11, 13]
array2 = [27, 89, 21, 78, 24, 75, 43, 87, 15]


def cuadratica(n):
    for i in range(len(n)):
        for j in range(len(n) - i - 1):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]
    return n[0]


print(cuadratica(array2))


def lineal(n):
    numMin = n[0]
    for i in range(1, len(n)):
        if numMin > n[i]:
            numMin = n[i]


print(cuadratica(array2))
