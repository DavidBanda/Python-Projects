from DS.Queue import Queue


def papaCal(listaDeNombres, N):

    Q = Queue()

    for nombre in listaDeNombres:
        Q.agregarItem(nombre)

    while Q.tamaño() > 1:
        for i in range(N):
            Q.agregarItem(Q.avanzar())
        Q.avanzar()

    return Q.avanzar()


print(papaCal(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 7))





