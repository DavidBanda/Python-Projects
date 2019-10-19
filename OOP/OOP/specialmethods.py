class Employee:

    raise_amount = 1.04

    def __init__(self, firstN, lastN, pay):
        self.firstN = firstN
        self.lastN = lastN
        self.pay = pay
        self.email = firstN.lower() + lastN.lower() + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.firstN, self.lastN)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', {}, '{}')".format(self.firstN, self.lastN,
                                                       self.pay, self.email)
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('David', 'Banda', 50000)
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1)

# print(str(emp_1))
# print(repr(emp_1))

print(emp_1.__str__())
print(emp_1.__repr__())

# print(1 + 2)
# print(int.__add__(1, 2))
# print(str.__add__('a', 'b'))

print("add", emp_1 + emp_2)

# print(len('test'))
# print('test'.__len__())
print(emp_1.__len__())
print(len(emp_1))

