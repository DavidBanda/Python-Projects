# li = [9, 3, 7, 8, 6, 2, 1, 0, 3]

# s_li = sorted(li, reverse=True)  # return a sorted list

# print('unsorted list:\t', li)
# print('sorted list:\t', s_li)
# li.sort(reverse=True)  # sort the current list and return none
# print('sorted list:\t', li)

###########################################################################

# tup = (9, 3, 7, 8, 6, 2, 1, 0, 3)
# s_tup = sorted(tup)
# print('tup sorted list:\t', s_tup)

# di = {'name': 'David', 'job': 'programming', 'age': None, 'os': 'Mac'}
# s_di = sorted(di)
# print('dict sorted list:\t', s_di)

###########################################################################

# li = [-6, -5, -4, 1, 2, 3]
# s_li = sorted(li, key=abs)
# print(s_li)

###########################################################################


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({}, {}, ${})'.format(self.name, self.age, self.salary)

from operator import attrgetter

e1 = Employee('Zarai', 23, 70000)
e2 = Employee('David', 25, 50000)
e3 = Employee('Aaron', 27, 60000)

employees = [e1, e2, e3]


def e_sort(emp):
    return emp.age


# s_employees = sorted(employees, key=e_sort)
# s_employees = sorted(employees, key=lambda e: e.name)
s_employees = sorted(employees, key=attrgetter('name'))
print(s_employees)


