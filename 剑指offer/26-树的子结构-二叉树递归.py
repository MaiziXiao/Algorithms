# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        """
        输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

        B是A的子结构， 即 A中有出现和B相同的结构和节点值。

        例如:
        给定的树 A:

             3
            / \
           4   5
          / \
         1   2
        给定的树 B：

           4 
          /
         1
        返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。
        """


        # 1、 判断A当前节点开始，B是否为子结构，如果不是看下A的左子树节点，如果也不是再看下A的右子树。
        # 2、如果是某节点开始A与B的起始节点重合：
        # ①判断B是否匹配完了，如果匹配完了说明为子结构
        # ②如果A匹配完了，或者A的值和B和值不等，直接返回False
        # ③如果当前点相同，那同时看一下左子树和右子树的情况。
        if A==None or B==None:
            return False

        def is_Subtree(A, B):
            # B完了说明A包含B
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            # 判断A和B的子树是否相等
            return is_Subtree(A.left, B.left) and is_Subtree(A.right, B.right)

        return is_Subtree(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
