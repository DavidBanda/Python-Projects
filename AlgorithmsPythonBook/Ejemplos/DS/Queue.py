class Queue:

    def __init__(self):
        self.array = []

    def agregarItem(self, item):
        self.array.insert(0, item)

    def avanzar(self):
        return self.array.pop()

    def estaVacia(self):
        return self.array == []

    def tamaño(self):
        return len(self.array)


if __name__ == '__main__':

    c = Queue()
    print(c.estaVacia())
    c.agregarItem(4)
    c.agregarItem('perro')
    c.agregarItem(True)
    print(c.tamaño())
    print(c.estaVacia())
    c.agregarItem(8.4)
    print(c.avanzar())
    print(c.avanzar())
    print(c.tamaño())



