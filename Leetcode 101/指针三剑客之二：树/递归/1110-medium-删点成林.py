from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        """
        给出二叉树的根节点 root，树上每个节点都有一个不同的值。

        如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。

        返回森林中的每棵树。你可以按任意顺序组织答案。
        """
        # 本题需要判断的东西有三样，第一该节点是否需要删除；
        # 第二该节点是否含有父节点，若不含有父节点，该节点便形成一个新的树。
        # 第三判断该节点的位置，是位于左子树还是右子树。
        ans = []
        ds = set(to_delete)

        def process(n):
            if not n:
                return None
            n.left, n.right = process(n.left), process(n.right)
            if n.val not in ds:
                return n
            # n.val在list中，把左右子树加到list里形成新的树
            if n.left:
                ans.append(n.left)
            if n.right:
                ans.append(n.right)
            return None

        root = process(root)
        # Root不在List中
        if root:
            ans.append(root)
        return ans
