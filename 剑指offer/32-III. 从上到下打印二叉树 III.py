from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。


        例如:
        给定二叉树:[3,9,20,null,null,15,7],

            3
           / \
          9  20
            /  \
           15   7
        返回其层次遍历结果：

        [
          [3],
          [20,9],
          [15,7]
        ]

        """
        if not root:
            return []
        queue = [root]
        next_level = []
        res = []
        temp = []
        layer = 1
        while queue:
            root = queue.pop(0)
            temp.append(root.val)
            if root.left:
                next_level.append(root.left)
            if root.right:
                next_level.append(root.right)
            # If queue is empty
            if not queue:
                if layer % 2 == 0:
                    res.append(temp[::-1])
                else:
                    res.append(temp)
                layer += 1
                queue = next_level
                temp = []
                next_level = []
        return res

        # if not root:
        #     return []
        # res = []
        # queue = [root]
        # tmp = []
        # next_layer = []
        # # 0 or 1
        # pop_order = 0
        # while queue:
        #     root = queue.pop(-1)
        #     tmp.append(root.val)
        #     if pop_order == 0:
        #         if root.left:
        #             next_layer.append(root.left)
        #         if root.right:
        #             next_layer.append(root.right)
        #     else:
        #         if root.right:
        #             next_layer.append(root.right)
        #         if root.left:
        #             next_layer.append(root.left)
        #     # queue empty
        #     if not queue:
        #         res.append(tmp)
        #         queue = next_layer
        #         tmp = []
        #         next_layer = []
        #         pop_order = 1 - pop_order
        #
        # return res
