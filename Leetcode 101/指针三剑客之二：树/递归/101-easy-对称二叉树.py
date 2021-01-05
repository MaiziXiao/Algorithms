# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        给定一个二叉树，检查它是否是镜像对称的。
        例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
        """
        # 递归的函数要干什么？
        # 函数的作用是判断传入的两个树是否镜像。
        # 输入：TreeNode left, TreeNode right
        # 输出：是：true，不是：false
        # 递归停止的条件是什么？
        # 左节点和右节点都为空 -> 倒底了都长得一样 ->true
        # 左节点为空的时候右节点不为空，或反之 -> 长得不一样-> false
        # 左右节点值不相等 -> 长得不一样 -> false
        # 从某层到下一层的关系是什么？
        # 要想两棵树镜像，那么一棵树左边的左边要和二棵树右边的右边镜像，一棵树左边的右边要和二棵树右边的左边镜像
        # 调用递归函数传入左左和右右
        # 调用递归函数传入左右和右左
        # 只有左左和右右镜像且左右和右左镜像的时候，我们才能说这两棵树是镜像的
        # 调用递归函数，我们想知道它的左右孩子是否镜像，传入的值是root的左孩子和右孩子。这之前记得判个root == null
        def node_symmetric(left, right):
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False
            elif left.val != right.val:
                return False
            # 左边的左边和右边的右边，左边的右边和右边的左边
            return node_symmetric(left.left, right.right) and node_symmetric(left.right, right.left)

        if not root:
            return True
        return node_symmetric(root.left, root.right)

        # BFS,左右各一个queue
        # if not root:
        #     return True
        # queuel, queuer = [root.left], [root.right]
        # while len(queuel) > 0 and len(queuer) > 0:
        #     left = queuel.pop()
        #     right = queuer.pop()
        #     # 都空的时候，相等或对称
        #     if not left and not right:
        #         continue
        #     # 一个空一个不空，不相等不对称
        #     elif not left or not right:
        #         return False
        #     if left.val != right.val:
        #         return False
        #     queuel.insert(0, left.left)
        #     queuel.insert(0, left.right)
        #     queuer.insert(0, right.right)
        #     queuer.insert(0, right.left)
        # return len(queuel) == 0 and len(queuer) == 0