from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = []
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

        例如:
        给定二叉树:[3,9,20,null,null,15,7],

            3
           / \
          9  20
            /  \
           15   7
        返回其层次遍历结果：

        [
          [3],
          [9,20],
          [15,7]
        ]
        """
        if not root:
            return []
        queue = [root]
        next_level = []
        res = []
        temp = []

        while queue:
            root = queue.pop(0)
            temp.append(root.val)
            if root.left:
                next_level.append(root.left)
            if root.right:
                next_level.append(root.right)
            # If queue is empty
            if not queue:
                res.append(temp)
                queue = next_level
                temp = []
                next_level = []
        return res
