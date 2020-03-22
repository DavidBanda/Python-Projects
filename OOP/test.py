class Persona:
    pass


per_1 = Persona()
per_1.nombre = "David Banda"
per_1.edad = 23


def getEdad(self):
    return self.edad


per_1.getEdad = getEdad(per_1)

print(f'nombre: {per_1.nombre}, edad: {per_1.edad}')
per_2 = Persona()
print(f'nombre: {per_2.nombre}, edad: {per_2.edad}')


def getEdad(self):
    return self.edad


