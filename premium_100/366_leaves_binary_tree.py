# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def getHeight(node):
            if not node:
                return -1
            
            left = getHeight(node.left)
            right = getHeight(node.right)
            curHeight = max(left, right) +1
            if len(result)==curHeight:
                result.append([])
            
            result[curHeight].append(node.val)
            return curHeight
        
        getHeight(root)
        return result