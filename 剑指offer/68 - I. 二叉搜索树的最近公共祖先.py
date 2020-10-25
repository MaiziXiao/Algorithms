# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

        百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
        满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
        """
        # 如果p, q 在root 左右两边，则root即是公共节点
        if p.val < root.val and q.val < root.val:
            root = root.left
            return self.lowestCommonAncestor(root, p, q)
        if p.val > root.val and q.val > root.val:
            root = root.right
            return self.lowestCommonAncestor(root, p ,q)
        else:
            return root