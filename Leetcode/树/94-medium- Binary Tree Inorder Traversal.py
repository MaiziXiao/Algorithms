from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
         1. 递归法可以一行代码完成，无需讨论；
         2. 迭代法一般需要通过一个栈保存节点顺序，我们这里直接使用列表
           - 首先，我要按照中序遍历的顺序存入栈，这边用的逆序，方便从尾部开始处理
           - 在存入栈时加入一个是否需要深化的参数
           - 在回头取值时，这个参数应该是否，即直接取值
           - 简单调整顺序，即可实现前序和后序遍历
         """
        # 递归法
        # if root is None:
        #     return []
        # return self.inorderTraversal(root.left)\
        #     + [root.val]\
        #     + self.inorderTraversal(root.right)
        # 迭代法
        result = []
        stack = [(1, root)]
        while stack:
            go_deeper, node = stack.pop()
            if node is None:
                continue
            if go_deeper:
                # 左右节点还需继续深化，并且入栈是先右后左
                stack.append((1, node.right))
                # 节点自身已遍历，回头可以直接取值
                stack.append((0, node))
                stack.append((1, node.left))
            else:
                result.append(node.val)
        return result
