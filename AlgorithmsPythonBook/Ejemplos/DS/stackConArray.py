class Stack:

    def __init__(self):
        self.items = []

    def incluir(self, item):
        self.items.append(item)

    def extraer(self):
        return self.items.pop()

    def inspeccionar(self):
        return self.items[-1]

    def estaVacia(self):
        return self.items == []

    def tamaño(self):
        return len(self.items)


def verificarSimbolos(cadenaSimbolos):

    p1 = Stack()
    for i in range(len(cadenaSimbolos)):
        if cadenaSimbolos[i] in "([{":
            p1.incluir(cadenaSimbolos[i])
        elif cadenaSimbolos[i] in ")]}":
            if p1.estaVacia():
                return False
            if parejas(p1.inspeccionar(), cadenaSimbolos[i]):
                p1.extraer()

    if p1.estaVacia():
        return True
    return False


def parejas(simboloApertura, simboloCierre):
    aperturas = "([{"
    cierres = ")]}"
    return aperturas.index(simboloApertura) == cierres.index(simboloCierre)


if __name__ == '__main__':
    print(verificarSimbolos('((()))'))
    print(verificarSimbolos('())'))
    print(verificarSimbolos('{{([][])}()}'))
    print(verificarSimbolos('[{()]'))




