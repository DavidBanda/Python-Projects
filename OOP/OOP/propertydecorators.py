class Employee:

    def __init__(self, firstN, lastN):
        self.firstN = firstN
        self.lastN = lastN

    @property
    def email(self):
        return '{}{}@gmail.com'.format(self.firstN, self.lastN)

    @property
    def fullname(self):
        return '{} {}'.format(self.firstN, self.lastN)

    @fullname.setter
    def fullname(self, name):
        firstN, lastN = name.split(' ')
        self.firstN, self.lastN = firstN, lastN

    @fullname.deleter
    def fullname(self):
        print('Delete Name!!')
        self.firstN = None
        self.lastN = None


emp_1 = Employee('John', 'Smith')

emp_1.fullname = 'David Banda'

print(emp_1.firstN)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

print(emp_1.fullname)

