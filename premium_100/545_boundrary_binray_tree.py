# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if root.right == None and root.left == None:
            return [root.val]
        left = []
        cur = root
        while True:
            left.append(cur.val)
            if cur.left:
                cur = cur.left
            elif cur.right:
                cur = cur.right
            elif cur.right == None and cur.left == None:
                break
        if root.left == None: left = [root.val]
        else:
            left=left[:-1]
        stack = [root]
        leaves = []
        while stack:
            cur = stack.pop()
            if cur.left == None and cur.right == None:
                leaves.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        right = []
        cur = root
        while True:
            right.append(cur.val)
            if cur.right:
                cur = cur.right
            elif cur.left:
                cur = cur.left
            elif cur.right == None and cur.left == None:
                break
        if root.right == None:
            right = []
        else:
            right = right[::-1][1:-1]
        return left + leaves + right