# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
        """

        def helper(root):
            """
            Decide if the root is a balanced Tree
            """
            # 后序遍历
            if not root:
                return 0
            ldepth = helper(root.left)
            rdepth = helper(root.right)
            # 如果子树已经不平衡，没必要继续算
            if ldepth is False or rdepth is False:
                return False
            # 看左子树右子树高度差是不是小于等于1
            if abs(ldepth - rdepth) <= 1:
                return max(ldepth, rdepth) + 1
            else:
                return False

        if helper(root) is False:
            return False
        else:
            return True
