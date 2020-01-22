# Sumar todos los numeros de i hasta n

# sumaFor recorre el array para acumular el valor en 'suma', por lo que el
# Big O es (n)


def sumaFor(n):

    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma


print("sumaFor: ", sumaFor(10))


# sumaEcuacion aplica una ecuacion cerrada para obtener la suma de todos
# los valores anteriores, obteniendo un Big O de (1)


def sumaEcuacion(n):
    return (n * (n + 1)) / 2


print("sumaEcuacion: ", int(sumaEcuacion(10)))

