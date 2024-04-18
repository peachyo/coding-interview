"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return root
        root2 = Node(root.val)
        queue = deque([(root, new_root)])
        while q:
            old_node, new_node = q.popleft()
            for child_node in old_node.children:
                new_child_node = Node(child_node.val)
                new_node.children.append(new_child_node)
                queue.append((child_node, new_child_node))
        return new_root
    
    def cloneTree(self, root: 'Node') -> 'Node':

        # Base case: empty node.
        if not root:
            return root

        # First, copy the node itself.
        node_copy = Node(root.val)

        # Then, recursively clone the sub-trees.
        for child in root.children:
            node_copy.children.append(self.cloneTree(child))

        return node_copy