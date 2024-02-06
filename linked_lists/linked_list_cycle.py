"""
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked
list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that
can be reached again by continuously following the next pointer. Internally,
pos is used to denote the index of the node that tail's next pointer is
connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    @staticmethod
    def from_list(arr, pos=-1):

        result = None
        cycle = None
        current = 0
        if arr is not None and len(arr) > 0:
            node = ListNode(val=arr.pop(0))
            result = node
            if pos == current:
                cycle = node
                print(cycle.val)
            for elem in arr:
                node.next = ListNode(val=elem)
                node = node.next

                current += 1
                if pos == current:
                    cycle = node
                    print(cycle.val)
            if pos != -1:
                node.next = cycle
                print('cycling', cycle.val)
        return result

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = set()
        temp = head
        while (temp):
            if (temp in s):
                return True
            s.add(temp)
            temp = temp.next
        return False


if __name__ == '__main__':
    s = Solution()
    l1 = [2, 4, 3, 7, 8]

    list_1 = Solution.from_list(l1, 1)
    cycles = s.hasCycle(list_1)
    print(cycles)