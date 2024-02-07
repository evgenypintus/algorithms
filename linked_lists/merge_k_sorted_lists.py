"""
23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
"""
class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(l1, l2):
    result = None
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.val < l2.val:
        result = l1
        result.next = merge_two_lists(l1.next, l2)
    else:
        result = l2
        result.next = merge_two_lists(l1, l2.next)
    return result

def merge_two_lists_cycle(l1, l2):

    current = ListNode()

    result = current
    while True:
        if l1 is None and l2 is None:
            break

        if l2 is None or l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    return result.next


def merge_k_lists(lists):
    if len(lists) == 0:
        return None
    if len(lists) == 1:
        return lists[0]
    if len(lists) == 2:
        return merge_two_lists(lists[0], lists[1])
    mid = len(lists) // 2
    left = merge_k_lists(lists[:mid])
    right = merge_k_lists(lists[mid:])
    return merge_two_lists(left, right)

def merge_k_lists_cycle(lists):
    if len(lists) == 0:
        return None
    if len(lists) == 1:
        return lists[0]

    result = lists[0]

    for l in lists[1:]:
        result = merge_two_lists(result, l)

    return result

def from_list(arr):
    result = None
    if arr is not None:
        node = ListNode(val=arr.pop(0))
        result = node
        for elem in arr:
            node.next = ListNode(val=elem)
            node = node.next
    return result

def to_list(l):
    node = l
    nodes = []
    while node is not None:
        nodes.append(node.val)
        node = node.next
    return nodes

list_1 = [1, 4, 5, 5]
list_2 = [0, 1, 3, 4, 4, 5]
list_3 = [1,2,3]

l1 = from_list(list_1)
l2 = from_list(list_2)
l3 = from_list(list_3)

# r = merge_k_lists_cycle([l1, l2, l3])
# r = merge_k_lists([l1, l2, l3])
r = merge_two_lists_cycle(l1, l2)
print(to_list(r))
