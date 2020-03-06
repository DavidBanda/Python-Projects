# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    @staticmethod
    def add_two_numbers(l1, l2):

        result_list = ListNode(0)
        current_list = result_list
        carry = 0

        while l1 or l2:

            res = (l1.value if l1 else 0) + (l2.value if l2 else 0)
            res += carryclosest
            carry, mod = divmod(res, 10)

            current_list.next = ListNode(mod)
            current_list = current_list.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return current_list.next











