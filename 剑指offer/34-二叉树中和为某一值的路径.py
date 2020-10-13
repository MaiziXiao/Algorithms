from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        """
        输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

        示例:
        给定如下二叉树，以及目标和sum = 22，

                      5
                     / \
                    4   8
                   /   / \
                  11  13  4
                 /  \    / \
                7    2  5   1
        返回:

        [
           [5,4,11,2],
           [5,8,4,5]
        ]
        """

        #         if not root:
        #             return []
        #         res = []
        #
        #         def helper(root: TreeNode, path, sum: int):
        #             sum = sum - root.val
        #             if root.left is None and root.right is None:
        #                 if sum == 0:
        #                     res.append(path)
        #                 return
        #             if root.left:
        #                 helper(root.left, path+[root.left.val], sum)
        #             if root.right:
        #                 helper(root.right, path+[root.right.val], sum)
        #
        #         helper(root,[root.val], sum)
        #
        #         return res

        if not root:
            return []
        res = []
        path = []
        def helper(root: TreeNode, sum: int):
            path.append(root.val)
            sum = sum - root.val
            if root.left is None and root.right is None:
                if sum == 0:
                    # path 一定要copy不然后面后修改
                    res.append(path[:])
                return
            if root.left:
                helper(root.left,  sum)
                path.pop()
            if root.right:
                helper(root.right,  sum)
                path.pop()

        helper(root, sum)
        return res
