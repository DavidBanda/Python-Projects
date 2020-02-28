arr = [1, 2, 3, 4, 5, 6]


def busqueda_secuencial(lista, item):

    i = [i for i in lista if i == item]

    return True if i else False


print(busqueda_secuencial(arr, 1))



