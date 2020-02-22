from Ejemplos.DS.stackConArray import Stack

def divideBy2(integer):

    if integer <= 0:
        return False

    s = Stack()
    bin = ''

    while integer >= 1:
        s.incluir(integer % 2)
        integer = integer // 2

    while not s.estaVacia():
        bin += f'{s.extraer()}'

    return bin


def baseConverter(integer, base):
    digits = "0123456789ABCDEF"

    if integer <= 0:
        return False

    s = Stack()
    bin = ''

    while integer >= 1:
        s.incluir(integer % base)
        integer = integer // base

    while not s.estaVacia():
        bin += f'{digits[s.extraer()]}'

    return bin


print(divideBy2(7))
print(baseConverter(233, 2))
print(baseConverter(8, 8))
print(baseConverter(16, 16))

