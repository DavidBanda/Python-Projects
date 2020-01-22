class Element:

    def __init__(self, value=None):
        self.value = value
        self.base = None

    def __str__(self):
        return str(self.value)


class Stack:

    def __init__(self, top=None):
        self.top = top
        if self.top is None:
            self.count = 0
        else:
            self.count = 1

    def incluir(self, item):
        self.count += 1
        if self.top is None:
            self.top = item
        else:
            temp = self.top
            self.top = item
            self.top.base = temp

    def tamaño(self):
        return self.count

    def estaVacio(self):
        if self.count == 0:
            return True
        return False

    def inspeccionar(self):
        return self.top

    def extraer(self):
        self.count -= 1
        temp = self.top
        self.top = self.top.base
        return temp


e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

s1 = Stack(e1)

s1.incluir(e2)

s1.incluir(e3)

s1.incluir(e4)

print(s1.estaVacio())
print(s1.tamaño())
print(s1.inspeccionar())

print(s1.extraer())
print(s1.inspeccionar())
print(s1.extraer())
print(s1.inspeccionar())



