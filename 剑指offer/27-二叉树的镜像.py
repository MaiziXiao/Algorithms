# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        """
        请完成一个函数，输入一个二叉树，该函数输出它的镜像。

        例如输入：

             4
           /   \
          2     7
         / \   / \
        1   3 6   9
        镜像输出：
             4
           /   \
          7     2
         / \   / \
        9   6 3   1

        示例 1：
        输入：root = [4,2,7,1,3,6,9]
        输出：[4,7,2,9,6,3,1]
        """
        # 条件跳出，不是while
        if not root:
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.mirrorTree(root.right)
        self.mirrorTree(root.left)
        return root