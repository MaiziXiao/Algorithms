# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        """
            给定一个二叉树，它的每个结点都存放着一个整数值。
            找出路径和等于给定数值的路径总数。
            路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
            二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

            示例：
            root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

                10
              5   -3
            3   2   11
        3  -2   1

            返回 3。和等于 8 的路径有:

            1.  5 -> 3
            2.  5 -> 2 -> 1
            3.  -3 -> 11
        """
        if not root:
            return 0
        # 加根节点的话，下面每一个都要加，不加的话可以从下一节点开始
        return self.pathSumWithRoot(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def pathSumWithRoot(self, root, sum):
        res = 0
        if not root:
            return res
        sum -= root.val
        if sum == 0:
            res += 1
        res += self.pathSumWithRoot(root.left, sum)
        res += self.pathSumWithRoot(root.right, sum)
        return res
