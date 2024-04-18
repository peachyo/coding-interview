# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.max_val = 1

        def dfs(node):
            if not node:
                return 1
            
            left=dfs(node.left)
            right =dfs(node.right)

            if node.left:
                if node.left.val-node.val!=1:
                    left = 1
                else:
                    left+=1

            if node.right:
                if node.right.val - node.val != 1:
                    right = 1
                else:
                    right += 1

            self.max_val = max(self.max_val, max(left, right))
            return max(left, right)
        dfs(root)
        return self.max_val
        
                
        
                