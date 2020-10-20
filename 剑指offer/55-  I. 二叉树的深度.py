# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度
        """
        # BFS
        # stack = [root]
        # next_layer = []
        # max_depth = 1
        # while len(stack) > 0:
        #     node = stack.pop(0)
        #     if node.left:
        #         next_layer.append(node.left)
        #     if node.right:
        #         next_layer.append(node.right)
        #     if len(stack) == 0:
        #         max_depth += 1
        #         stack = next_layer
        #
        # return max_depth

        # 递归
        if root == None:
            return 0
        ldepth = Solution.maxDepth(self, root.left)
        rdepth = Solution.maxDepth(self, root.right)
        return max(ldepth, rdepth) + 1