from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

        例如，给出

        前序遍历 preorder = [3,9,20,15,7]
        中序遍历 inorder = [9,3,15,20,7]
        返回如下的二叉树：

            3
           / \
          9  20
            /  \
           15   7

        """
        # 思路 https://zhuanlan.zhihu.com/p/73438175
        if not preorder:
            return None
        loc = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        # 前序和中序遍历左子树都是在list的前一半，所以可以用中序的index去index前序的List
        root.left = self.buildTree(preorder[1 : loc + 1], inorder[0:loc])
        root.right = self.buildTree(preorder[loc + 1 :], inorder[loc + 1 :])
        return root