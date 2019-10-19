class Example:

    def add(self, x, y):
        self.added = x + y
        print(self.added)

    def res(self, x, y):
        self.sub = x - y
        print(self.sub)

    def imp(self):
        print(self.added)

class Example2:
    def add(x, y):
        added = x + y
        print(added)

    def res(x, y):
        sub = x - y
        print(sub)

obj1 = Example()
obj1.add(4, 2)
y = obj1.imp()

#Example2.add(4, 2)
