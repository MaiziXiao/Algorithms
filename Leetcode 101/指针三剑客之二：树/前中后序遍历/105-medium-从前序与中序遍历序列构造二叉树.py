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
        根据一棵树的前序遍历与中序遍历构造二叉树。
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : index + 1], inorder[0:index])  # noqa
        root.right = self.buildTree(preorder[index + 1 :], inorder[index + 1 :])  # noqa
        return root
