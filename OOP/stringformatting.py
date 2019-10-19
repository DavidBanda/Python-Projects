person = {'name': 'David', 'age': 23}
l = ['David', 23]

# sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
# print(sentence)

# sentence = 'My name is {0} and I am {1} years old. {0} - {1}'.format(person['name'], person['age'])
# print(sentence)

# tag = 'h1'
# text = 'This is a headline'

# sentence = '<{0}>{1}</{0}>'.format(tag, text)
# print(sentence)

# sentence = 'My name is {0[0]} and I am {0[1]} years old. {0[0]} - {0[1]}'.format(l)
# print(sentence)

'''
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
'''

# p1 = Person('Jack', '33')
# sentence = 'My name is {0.name} and I am {0.age} years old. {0.name} - {0.age}'.format(p1)
# print(sentence)

# sentence = 'My name is {name} and I am {age} years old. {name} - {age}'.format(name='David', age='23')
# print(sentence)

# unpack dict
# sentence = 'My name is {name} and I am {age} years old. {name} - {age}'.format(**person)
# print(sentence)

'''
for i in range(1, 11):
    sentence = 'The value is {:02}'.format(i)
    print(sentence)
'''

# pi = 3.14159265
# sentence = 'The value is {:.3f}'.format(pi)
# print(sentence)

# sentence = '1MB is equal to {:,.2f} bytes'.format(1000**2)
# print(sentence)

import datetime
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print(my_date)

sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the ' \
           'year'.format(my_date)
print(sentence)

