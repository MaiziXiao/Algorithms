# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        给定一个二叉树，找出其最大深度。
        二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
        说明: 叶子节点是指没有子节点的节点。
        示例：
        给定二叉树 [3,9,20,null,null,15,7]，
        3
        / \
        9  20
            /  \
        15   7
        """
        if not root:
            return 0
        self.maxdepth = 1

        def helper(head, cur_depth):
            if not head:
                return
            if not head.left and not head.right:
                self.maxdepth = max(self.maxdepth, cur_depth)
                return
            helper(head.left, cur_depth + 1)
            helper(head.right, cur_depth + 1)

        helper(root, 1)

        return self.maxdepth

        # 网上解法
        # DFS
        # 叶节点是0，一个一个往上加上去
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # # BFS
        # if not root:
        #     return 0

        # depth = 0
        # q = [root]
        # while len(q) != 0:
        #     depth += 1
        #     for i in range(0, len(q)):
        #         if q[0].left:
        #             q.append(q[0].left)
        #         if q[0].right:
        #             q.append(q[0].right)
        #         q.pop(0)
        # return depth
