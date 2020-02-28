from add_two_numbers.linked_list import Element, LinkedList

l1 = LinkedList()
l2 = LinkedList()

e1 = Element(2)
e2 = Element(4)
e3 = Element(3)

e4 = Element(5)
e5 = Element(6)
e6 = Element(4)

l1.append(e1)
l1.append(e2)
l1.append(e3)

l2.append(e4)
l2.append(e5)
l2.append(e6)


class Solution:

    def add_two_numbers(self, list1, list2):
        l3 = LinkedList()
        add = self.to_integer(list1) + self.to_integer(list2)
        add = f'{add}'
        add = add[::-1]

        for i in range(len(add)):
            e = Element(int(add[i]))
            l3.append(e)
        print(l3.print_all_list())
        return l3

    @staticmethod
    def to_integer(lst):
        current = lst.head
        value = f'{current.value}'
        while current.next:
            current = current.next
            value += f'{current.value}'
        return int(value[::-1])


s = Solution()
s.add_two_numbers(l1, l2)







