class Employee:

    raise_amount = 1.04

    def __init__(self, firstN, lastN, pay):
        self.firstN = firstN
        self.lastN = lastN
        self.pay = pay
        self.email = firstN.lower() + lastN.lower() + '@gmail.com'

    def fullnamef(self):
        return f'{self.firstN} {self.lastN}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_amt(cls, amount):
        cls.raise_amount = amount


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, firstN, lastN, pay, prog_lang):
        super().__init__(firstN, lastN, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, firstN, lastN, pay, employees=None):
        super().__init__(firstN, lastN, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullnamef())


emp_1 = Employee('David', 'Banda', 50000)
emp_2 = Employee('Test', 'User', 60000)

dev_1 = Developer('Aaron', 'Gutierrez', 100000, 'Python')
dev_2 = Developer('Test', 'Dev', 110000, 'Java')

lst = [emp_1, emp_2, dev_1, dev_2]

man_1 = Manager('Jose', 'Fernandez', 500000, lst)

# man_1.print_emps()

print(isinstance(man_1, Manager))
print(isinstance(man_1, Employee))
print(isinstance(man_1, Developer))

print('\n')

# if a class is a subclass of another
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Developer, Manager))

print(help(Developer))



