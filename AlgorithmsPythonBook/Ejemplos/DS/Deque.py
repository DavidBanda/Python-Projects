class Deque:

    def __init__(self):
        self.array = []

    def agregarFrente(self, item):
        self.array.append(item)

    def agregarFinal(self, item):
        self.array.insert(0, item)

    def removerFrente(self):
        return self.array.pop()

    def removerFinal(self):
        return self.array.pop(0)

    def estaVacia(self):
        return self.array == []

    def tamaño(self):
        return len(self.array)


if __name__ == '__main__':
    d = Deque()
    print(d.estaVacia())
    d.agregarFinal(4)
    d.agregarFinal('perro')
    d.agregarFrente('gato')
    d.agregarFrente(True)
    print(d.tamaño())
    print(d.estaVacia())
    d.agregarFinal(8.4)
    print(d.removerFinal())
    print(d.removerFrente())




