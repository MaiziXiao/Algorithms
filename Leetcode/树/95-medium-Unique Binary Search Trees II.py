from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        """
        Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
        """
        # 在二叉搜索树中：
        # 1.若任意结点的左子树不空，则左子树上所有结点的值均不大于它的根结点的值。
        # 2.若任意结点的右子树不空，则右子树上所有结点的值均不小于它的根结点的值。
        # 3.任意结点的左、右子树也分别为二叉搜索树。
        # 只是我们需要求解的不仅仅是数字，而是要求解所有的组合。我们假设问题 f(1, n) 是
        # 求解 1 到 n（两端包含）的所有二叉树。那么我们的目标就是求解f(1, n)。
        # 我们将问题进一步划分为子问题，假如左侧和右侧的树分别求好了，我们是不是只要运用组合的原理，将左右两者进行做和就好了，
        # 们需要两层循环来完成这个过程。
        if not n:
            return []

        def generateTree(start, end):
            # left should be smaller than right
            if start > end:
                return [None]
            res = []
            for i in range(start, end + 1):
                ls = generateTree(start, i - 1)
                rs = generateTree(i + 1, end)
                for l in ls:
                    for r in rs:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        res.append(node)

            return res

        return generateTree(1, n)

print(Solution().generateTrees(3))