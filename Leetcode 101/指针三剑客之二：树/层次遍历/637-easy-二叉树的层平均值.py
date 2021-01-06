from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        """
        给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

        示例 1：

        输入：
            3
        9  20
          15   7
        输出：[3, 14.5, 11]
        """
        res = []
        que = [root]
        # 用一个que
        while len(que) > 0:
            count = len(que)
            sum = 0
            # 遍历一层节点时，当前队列节点数就是当前层的节点数，只要遍历这么多节点，就能保证这次遍历都是当前节点
            for _ in range(len(que)):
                node = que.pop(0)
                sum += node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(sum / count)
        return res
