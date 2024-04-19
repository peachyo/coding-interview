# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left_max = self.find_max(root.left)
        if left_max >= root.val:
            return False
        right_min = self.find_min(root.right)
        if right_min <= root.val:
            return False
        return self.is_valid_bst(root.left) and self.is_valid_bst(root.right)

    def find_max(self, root: Optional[TreeNode]) -> int:
        if not root:
            return float('-inf')
        return max(root.val, self.find_max(root.left), self.find_max(root.right))
    
    def find_min(self, root: Optional[TreeNode])-> int:
        if not root:
            return float('inf')
        return min(root.val, self.find_min(root.left), self.find_min(root.right))

    def count_nodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+ self.count_nodes(root.left) + self.count_nodes(root.right)
    
    def largestBSTSubtree(self, root:Optional[TreeNode]) -> int:
        if not root:
            return 0
        if self.is_valid_bst(root):
            return self.count_nodes(root)
        
        return max(self.largestBSTSubtree(root.left), 
        self.largestBSTSubtree(root.right))