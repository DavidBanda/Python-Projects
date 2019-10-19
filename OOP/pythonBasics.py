'''
Comentar varias lineas de codigo
'''

# Variables
'''
(x ,y, z) = (3, 5, 8)

print(x)
print(y)
print(z)

def func():
    return (3, 5, 8)

(x1, y1, z1) = func()

print('\n')
print(x1)
print(y1)
print(z1)
'''

# while loop
'''
condition = 1

while condition <= 10:
    print('Number:', condition)
    condition += 1
'''

# for loop
'''
exampleList = [9, 8, 4, 90, 56, 23, 95, 23]

for x in exampleList:
    print(x)

print('\n')

for x in range(1, 11):
    print(x)
'''

# if else elif statement
'''
x = 5
y = 6
z = 7

if x > y:
    print('true')
elif z > y:
    print('false')
elif x == y == z:
    print('wot')
else:
    print('super false')
'''

# functions
'''
def sum1(num1 = 2, num2 = 2):
    print('num1 =', num1, '\nnum2 =', num2, '\nla suma es:', num1+num2)
    print('\n')

sum1(num2 = 6, num1 = 5)
sum1()
'''

# global and local variables
'''
x = 6

def example():
    global x
    x += 2
    print(x)

example()

'''

# input
'''
x = input('Cual es tu nombre?: ')
print('Hola',x)
'''

# tuplas

# x = 9, 1, 4, 6, 1, 8, 9, 1, 9, 8

# print(x.count(1))
# print(x.index(9, 1, 7))
# print(x[2])


# lista
'''
x = [9, 1, 4, 6, 1, 8, 9, 1, 9, 8]
print(x)
x.append(10)
print(x)
x.insert(2, 15)
print(x)
x.pop(2)
print(x)
x.remove(1)
print(x)
y = x[0:4]
print(y)
'''
# multidimensional list

# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [[1, 4, 6], [9, 6, 5]]]
#
#
# print(x[3][1][2])
#
# print('''
# Sin ningun tipo de error
# ''')

# from statistics import *
# import statistics

'''
La diferencia radica en que la primera importa los modulos como si fueran locales
y la segunda crea un objeto donde podemos acceder a los modulos
'''

my_list = [1, 2, 3, 4, 5, 6, 7]

my_list = 'http://coreyms.com'

print(my_list[::-1])

# lambda

# lm = lambda x, y: x * y
# print(lm(5, 2))
