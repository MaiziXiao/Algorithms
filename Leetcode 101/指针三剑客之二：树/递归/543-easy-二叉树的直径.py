# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。
        这条路径可能穿过也可能不穿过根结点。

        示例 :
        给定二叉树[1,2,3,4,5]
        返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
        """
        self.diameter = 0
        if not root:
            return 0

        def helper(root) -> int:
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            # 更新值和返回值不同
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)

        helper(root)
        return self.diameter
