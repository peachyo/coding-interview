# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        q = []
        def inorder(node):
            return inorder(node.left) + [node.val] +inorder(node.right) if node else[]
        q=inorder(root)
        q.sort(key= lambda x: abs(x-target))
        return q[:k]

    def heap(self, root: TreeNode, target: float, k: int) -> List[int]:
        def dfs(node, heap):
            if not node:
                return
            
            heappush(heap, (-abs(node.val - target), node.val))
            if len(heap) > k:
                heappop(heap)

            dfs(node.left, heap)
            dfs(node.right, heap)
        
        heap = []
        dfs(root, heap)
        return [x[1] for x in heap]    