# 2046 sort linked list already sorted using absolute vaules

# idea is to put negative vault on the left side
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sort_linkedlist(head):
    head = ListNode()
    neg = prev = head
    curr = head.next
    while curr:
        if curr.val < 0:
            prev.next = curr.next
            curr.next = neg
            neg = curr
            curr = prev.next
        else:
            prev, curr = curr, curr.next

    return neg
