class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return self.val


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = ListNode(val=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = ListNode(val=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.val)
            node = node.next
        return nodes

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def to_list(self):
        result = []
        for i in self:
            result.append(i.val)
        return result

    def get_number_reversed(self):
        number = 0
        arr = self.to_list()
        for l in arr[::-1]:
            number = l + number * 10
        return number

    @staticmethod
    def get_list(number):
        array = [int(x) for x in str(number)]
        return array