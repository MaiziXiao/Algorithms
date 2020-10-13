"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.last_node = None
        self.head = None

        def helper(root):
            if not root:
                return
            helper(root.left)
            # 下面两个判断很重要，因为起始的时候last node是None所以不要连接，但是之后last none右节点要连现在的点
            # Head
            if not self.last_node:
                self.head = root
            else:
                self.last_node.right = root
            root.left = self.last_node
            self.last_node = root
            helper(root.right)

        helper(root)
        self.head.left = self.last_node
        self.last_node.right = self.head
        return self.head