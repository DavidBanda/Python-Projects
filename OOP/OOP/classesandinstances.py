class Employee:
    pass


emp_1 = Employee()
emp_2 = Employee()

# print(emp_1)
# print(emp_2)

# instance variables

emp_1.firstN = 'David'
emp_1.lastN = 'Banda'
emp_1.email = 'davidbandag96@gmail.com'
emp_1.pay = 50000

emp_2.firstN = 'Test'
emp_2.lastN = 'User'
emp_2.e2ail = 'testuser@gmail.com'
emp_2.pay = 60000

# print(emp_1.firstN, emp_1.lastN)
# print(emp_2.firstN, emp_2.lastN)

######################################################################


class Employee2:

    def __init__(self, firstN, lastN, pay):
        self.firstN = firstN
        self.lastN = lastN
        self.pay = pay
        self.email = firstN.lower() + lastN.lower() + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.firstN, self.lastN)

    def fullnamef(self):
        return f'{self.firstN} {self.lastN}'


emp_2_1 = Employee2('David', 'Banda', 50000)
emp_2_2 = Employee2('Test', 'User', 60000)

print(emp_2_1.email)
print(emp_2_2.email)

# print(emp_2_1.fullname())
# print(emp_2_2.fullnamef())

print(Employee2.fullname(emp_2_2))

######################################################################

