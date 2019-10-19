class Element:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def printAllList(self):
        current = self.head
        if self.head:
            print(current.value)
            while current.next:
                current = current.next
                print(current.value)

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        current = self.head
        if self.head and position > 0:
            for n in range(1, position):
                current = current.next
                if current is None:
                    break
            if current:
                return current
        else:
            return None

    def insert(self, new_element, position):
        if self.head:
            if position == 1:
                new_element.next = self.get_position(position)
                self.head = new_element
            else:
                new_element.next = self.get_position(position)
                previous = self.get_position(position - 1)
                if previous:
                    previous.next = new_element

    def delete(self, value):
        current = self.head
        previous = None

        while current.value != value and current.next:
            previous = current
            current = current.next

        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next


e1 = Element(3)
e2 = Element(5)
e3 = Element(7)
e4 = Element(9)
e5 = Element(11)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)

ll.printAllList()
print("\nGet position:", ll.get_position(3).value, "\n")
ll.insert(e5, 1)
ll.printAllList()
ll.delete(3)
print("")
ll.printAllList()
