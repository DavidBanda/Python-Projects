class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, firstN, lastN, pay):
        self.firstN = firstN
        self.lastN = lastN
        self.pay = pay
        self.email = firstN.lower() + lastN.lower() + '@gmail.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.firstN, self.lastN)

    def fullnamef(self):
        return f'{self.firstN} {self.lastN}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('David', 'Banda', 50000)
emp_2 = Employee('Test', 'User', 60000)

Employee.raise_amount = 1.05
emp_1.raise_amount = 1.06
Employee.raise_amount = 1.07

print("emp_1:", emp_1.raise_amount)
print("emp_2:", emp_2.raise_amount)
emp_1.apply_raise()
print("emp_1:", emp_1.pay)
emp_2.apply_raise()
print("emp_2:", emp_2.pay)

print(Employee.num_of_emps)

print('\n')
print(emp_1.__dict__)
print(emp_2.__dict__)
print(Employee.__dict__)


