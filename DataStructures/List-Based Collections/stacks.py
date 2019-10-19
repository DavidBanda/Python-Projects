class Element:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def printAllStack(self):
        current = self.head
        c = 0
        if self.head:
            while current.next:
                c += 1
                print(c, current.value)
                current = current.next
            c += 1
            print(c, current.value)

    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def delete(self):
        if self.head:
            temp = self.head
            self.head = self.head.next
            return temp

class Stack:
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        return self.ll.delete()

    def printAll(self):
        self.ll.printAllStack()

e1 = Element(3)
e2 = Element(5)
e3 = Element(7)
e4 = Element(9)
e5 = Element(11)

stack = Stack(e1)
stack.push(e2)
stack.push(e3)
stack.push(e4)

stack.printAll()
print("")
stack.pop()
stack.pop()
stack.printAll()