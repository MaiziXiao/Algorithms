# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        给定一个二叉树，判断它是否是高度平衡的二叉树。
        本题中，一棵高度平衡二叉树定义为：
        一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
        示例 1：


        输入：root = [3,9,20,null,null,15,7]
        输出：true
        """

        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            if left == -1 or right == -1 or not (-1 <= left - right <= 1):
                return -1
            return 1 + max(left, right)

        return helper(root) != -1
