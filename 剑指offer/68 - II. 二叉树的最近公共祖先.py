# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

        百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
        满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

        说明:
        所有节点的值都是唯一的。
        p、q 为不同节点且均存在于给定的二叉树中。
        """
        # 递归
        # 如果一个节点的左子树和右子树都不为空，那就说明该节点就是最近公共祖先
        # 如果左节点不为空，右节点为空，说明最近公共祖先在当前节点的左子树
        # 如果右节点不为空，左节点为空，说明最近公共祖先在当前节点的右子树
        # 关于返回值来说，判断左子树是否为空，为空就返回右子树，不为空就继续判断右子树是否为空，不为空说明这个root就是公共祖先，否则的话就返回不为空的节点。【判断左子树返回值是否为空，为空说明左子树没有找到p或者q，那就返回右节点(
        #     右节点如果不为空的话，就说明右子树找到了，为空的话那就是当前的root没有找到p或者q)，但其实递归的代码是不需要考虑那么多的，只需要知道什么情况是找到了节点什么时候是没有找到就好
        if not root: return None  # 叶子节点，直接返回空节点，也即root
        if p == root or q == root:  # 如果p、q中有一个是当前节点root，则直接返回当前节点
            return root  # 返回了节点p或者q
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:  # 如果左右子树的返回值都不为空，此时root为p、q的最近公共祖先，返回root
            return root

        # 如果这个节点不是公共祖先，那么它就从两颗子树那继承状态，并返回给上一级
        return left or right

        # 非递归，遍历根节点到p和到q的两个路径（注意剪枝） 然后两个路径逐个比对，最后一个相同的节点即为公共节点。
        stack1, stack2 = [], []
        ret = None

        def dfs(root, target, stack):
            if not root:
                return False
            stack.append(root)
            if root == target:
                return True
            if dfs(root.left, target, stack) or dfs(root.right, target, stack):
                return True
            stack.pop()

        dfs(root, p, stack1)
        dfs(root, q, stack2)

        length = min(len(stack1), len(stack2))
        for i in range(length):
            if stack1[i] == stack2[i]:
                ret = stack1[i]

        return ret