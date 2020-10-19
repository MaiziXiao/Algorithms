# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        """
        给定一棵二叉搜索树，请找出其中第k大的节点。
        """
        # 通过中序遍历所得到的序列，就是有序的。
        # 1.递归做法
        # result = []
        #
        # def helper(root):
        #     helper(root.right)
        #     result.append(root.val)
        #     helper(root.left)
        #
        # helper(root)
        # return result[-k]

        # 2. 非递归


        #     根据中序遍历的顺序，对于任一结点，优先访问其左孩子，而左孩子结点又可以看做一根结点，
        #     然后继续访问其左孩子结点，直到遇到左孩子结点为空的结点才进行访问，然后按相同的规则访问其右子树。因此其处理过程如下：
        #     对于任一结点P，
        #
        #   1)若其左孩子不为空，则将P入栈并将P的左孩子置为当前的P，然后对当前结点P再进行相同的处理；
        #   2)若其左孩子为空，则取栈顶元素并进行出栈操作，访问该栈顶结点，然后将当前的P置为栈顶结点的右孩子；
        #   3)直到P为NULL并且栈为空则遍历结束
        result = []
        stack = []
        pos = root
        while pos or len(stack) > 0:
            # 先一直往下走直到pos是None
            if pos:
                stack.append(pos)
                pos = pos.right
            else:
                pos = stack.pop()
                result.append(pos.val)
                if len(result) == k:
                    return result[-1]
                pos = pos.left


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

Solution().kthLargest(a, 5)