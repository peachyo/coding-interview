class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def rec(node):
            if node is None:
                return 1
            node.val += rec(node.next)
            if node.val == 10:
                node.val = 0
                return 1
            return 0
        if rec(head)==1:
            new_node = ListNode(1, head)
            return new_node
        return head