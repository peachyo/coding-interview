# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        q=[]
        def dfs(node):
            return dfs(node.left) + [target -node.val] + dfs(node.right) if node else []
        q=set(dfs(root1))
        print(q)
        def check(node):
            if not node:
                return False
            print(node.val)
            if node.val in q:
                return True
            return check(node.left) or check(node.right)

        return check(root2)