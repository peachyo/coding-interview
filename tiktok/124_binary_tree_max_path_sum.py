# 124. Binary Tree Maximum Path Sum
# 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

def maxPathSum(self, root: TreeNode) -> int:
    max_sum = float('-inf')

    def maxPath(node):
        nonlocal max_sum
        if not node:
            return 0
        left = max(0, maxPath(node.left))
        right = max(0, maxPath(node.right))
        max_sum = max(max_sum, left + right + node.val)
        return max(left, right) + node.val
    maxPath(root)
    return max_sum