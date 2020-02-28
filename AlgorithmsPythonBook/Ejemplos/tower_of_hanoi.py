pasos = 0


def moverTorre(altura, origen, intermedio, destino):
    if altura >= 1:
        moverTorre(altura - 1, origen, destino, intermedio)
        mover_hacia(origen, intermedio)
        moverTorre(altura - 1, destino, intermedio, origen)


def mi_torre_de_hanoi(altura, origen, intermedio, destino):
    if altura >= 1:
        mi_torre_de_hanoi(altura - 1, origen, destino, intermedio)
        mover_hacia(origen, destino)
        mi_torre_de_hanoi(altura - 1, intermedio, origen, destino)


def mover_hacia(desde, hacia):
    global pasos
    pasos += 1
    print(f'Paso {pasos}: mover desde {desde} hacia {hacia}')


# moverTorre(3, "A", "B", "C")
mi_torre_de_hanoi(7, 'A', 'B', 'C')

