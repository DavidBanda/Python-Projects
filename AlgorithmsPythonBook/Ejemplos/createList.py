# concatenación  6.54352807999 milisegundos
# append  0.306292057037 milisegundos
# comprensión  0.147661924362 milisegundos
# método range  0.0655000209808 milisegundos


def prueba1():
    l = []
    for i in range(1000):
        l = l + [i]


def prueba2():
    l = []
    for i in range(1000):
        l.append(i)


def prueba3():
    l = [i for i in range(1000)]


def prueba4():
    l = list(range(1000))






