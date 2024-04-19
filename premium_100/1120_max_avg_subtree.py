# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.max_avg = 0

        def dfs(node):
            if not node:
                return 0, 0
        
            left, left_count = dfs(node.left)
            right, right_count = dfs(node.right)
            total = right_count+left_count +1
            val = node.val+left+right
            self.max_avg=max(self.max_avg, val/total)
            return val, total
        dfs(root)
        return self.max_avg

