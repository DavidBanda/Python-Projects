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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('David', 'Banda', 50000)
# emp_2 = Employee('Test', 'User', 60000)

emp_str_1 = 'John-Doe-7000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

emp_2 = Employee.from_string(emp_str_1)
print(emp_2.__dict__)
print(emp_2.raise_amount)

import datetime

my_date = datetime.date(2016, 7, 10)
print(emp_1.is_workday(my_date))

