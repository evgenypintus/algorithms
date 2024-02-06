"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative
integers.
The digits are stored in reverse order, and each of their nodes contains a
single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.
"""


class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    @staticmethod
    def from_list(arr):
        result = None
        if arr is not None:
            node = ListNode(val=arr.pop(0))
            result = node
            for elem in arr:
                node.next = ListNode(val=elem)
                node = node.next
        return result

    @staticmethod
    def to_list(l):
        node = l
        nodes = []
        while node is not None:
            nodes.append(node.val)
            node = node.next
        return nodes

    @staticmethod
    def get_number_reversed(l):
        number = 0
        arr = Solution.to_list(l)
        for l in arr[::-1]:
            number = l + number * 10
        return number

    @staticmethod
    def get_list(number):
        array = [int(x) for x in str(number)]
        return array

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r = self.get_number_reversed(l1) + self.get_number_reversed(l2)
        return self.from_list(self.get_list(r)[::-1])


if __name__ == '__main__':
    s = Solution()
    l1 = [2, 4, 3, 7, 8]
    l2 = [1]

    list_1 = Solution.from_list(l1)
    list_2 = Solution.from_list(l2)

    r = s.addTwoNumbers(list_1, list_2)

    print(Solution.to_list(r))





