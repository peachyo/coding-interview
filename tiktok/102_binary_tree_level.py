# 102. Binary Tree Level Order Traversal
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):

    levels = []
    queue = deque()
    queue.append(root)
    level = 0

    while queue:
        levels.append([])
        for i in range(len(queue)):
            node = queue.popleft()
            levels[level].append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
            level+=1
    
    return levels
            

def levelOrderDfs(root):
    levels = []
    if not root:
        return levels
    
    def dfs(node, level):
        if len(levels)==level:
            levels.append([])

        levels[level].append(node.val)
        if node.left:
            dfs(node.left, level+1)
        if node.right:
            dfs(node.right, level+1)
    
    dfs(root,0)
    return levels