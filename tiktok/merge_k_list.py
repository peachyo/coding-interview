# 23 Merge K Sorted Lists
import heapq


# brute force
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge(lists):
    result = []
    head = ListNode()
    cur = head

    for ls in lists:
        while ls:
            result += ls.next

    result = sorted(result)
    for i in result:
        node = ListNode(i)
        cur.next = node
        cur = node

    return head.next


# compare pairs
def mergeKLists(lists):
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    mid = len(lists) // 2
    left = mergeKLists(lists[:mid])
    right = mergeKLists(lists[mid])

    return mergeHelper(left, right)

def mergeHelper(self, l1, l2):
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next

    curr.next = l1 or l2
    return dummy.next

# heap

