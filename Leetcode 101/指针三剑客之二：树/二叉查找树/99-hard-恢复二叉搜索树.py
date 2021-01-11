# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.

        给你二叉搜索树的根节点 root ，该树中的两个节点被错误地交换。请在不改变其结构的情况下，恢复这棵树。

        进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用常数空间的解决方案吗？
        示例 1：


        输入：root = [1,3,null,null,2]
        输出：[3,1,null,null,2]
        解释：3 不能是 1 左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。
        """
        # 中序遍历是有序的。
        # 那么，如果其中两个被交换了，那么中序遍历的结果一定也就不对了。比如：
        # [1, 2, 3, 4, 5, 6]  ==>  [1, 5, 3, 4, 2, 6]
        # 那么，可以看出5这个数字比后面的3大，说明他被打乱了；另外2这个数字，比前面的数字4小，所以他也被打乱了。
        # 所以，可以通过先进行中序遍历得到所有的，然后再查找哪些乱了，再复原，时间复杂度O(n)。
        # 但是，中序遍历的操作不需要完全完成。在中序遍历的过程中，用一个指针保存上个节点，
        # 那么当前节点值应该小于前一个节点的值。否则就存在乱序。
        # 第一个乱序的数字是pre，第二个乱序的数字是root，所以用两个指针分别保存。
        self.pre, self.first, self.second = None, None, None
        self.inOrder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        # 一直保存一个pre的指针
        # 如果只出现一次次序错误，说明这两个相邻节点要交换
        # 如果出现两次次序错误，要交换这两个节点
        # [1,3,2,4,5,6]遍历到2时，pre和first是3, second是2
        # [1, 4, 3, 2, 5, 6, 7]遍历到3时， pre和first是4。遍历到2时，因为已经有first了，second变成2。交换2和4
        if self.pre and self.pre.val > root.val:
            if not self.first:
                self.first = self.pre
            self.second = root
        self.pre = root
        self.inOrder(root.right)
