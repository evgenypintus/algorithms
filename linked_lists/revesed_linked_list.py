"""
206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the
reversed list.
"""
class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev
        return head

    @staticmethod
    def from_list(arr):

        result = None
        if arr is not None or len(arr) > 0:
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


if __name__ == '__main__':
    s = Solution()
    l1 = [2, 4, 3, 7, 8]

    list_1 = Solution.from_list(l1)

    r = s.reverseList(list_1)

    print(Solution.to_list(r))