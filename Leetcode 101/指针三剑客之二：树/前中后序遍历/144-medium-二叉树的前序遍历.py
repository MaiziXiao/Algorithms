from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = []

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

        示例 1：
        输入：root = [1,null,2,3]
        输出：[1,2,3]
        """
        # if not root:
        #     return
        # self.res.append(root.val)
        # self.preorderTraversal(root.left)
        # self.preorderTraversal(root.right)
        # return self.res

        # # 非递归前序
        # res = []
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         res.append(node.val)
        #         # 注意这里先加右边因为先进后出
        #         stack.append(node.right)
        #         stack.append(node.left)
        # return res

        # 非递归中序
        # 1、申请一个新的栈，记为stack，申请一个变量cur，初始时令stack为空,cur等于头节点。
        # 2、先把cur节点压入栈中，对以cur节点为头的整棵子树来说，依次把整棵树的左边界压入栈中，即不断令cur=cur.left，然后重复步骤2。
        # 3、不断重复步骤2，直到发现cur为空，此时从stack中弹出一个节点，记为node。打印node的值，并让cur=node.right，然后继续重复步骤2。
        # 4、当stack为空并且cur为空时，整个过程结束。
        # stack = []
        # cur = root
        # res = []
        # # 1.栈非空则还可以输出 2.栈空但是节点非空说明还有节点可以压栈（初始化的时候）
        # while stack or cur:
        #     if cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     # cur为None的时候说明到底了，这时候改打印一个值，然后指针指向该节点的右边
        #     else:
        #         # cur为空，此时从stack中弹出一个节点，记为node
        #         node = stack.pop()
        #         res.append(node.val)
        #         cur = node.right
        # return res

        # 非递归后序
        # 方法1
        # 1、申请一个栈，记为s1，然后将头节点压入s1中。
        # 2、从s1中弹出的节点记为cur，然后先把cur的左孩子压入s1中，然后把cur的右孩子压入s1中。
        # 3、在整个过程中，每一个从s1中弹出的节点都放进第二个栈s2中。
        # 4、不断重复步骤2和步骤3，直到s1为空，过程停止。
        # 5、从s2中依次弹出节点并打印，打印的顺序就是后序遍历的顺序了。
        # 方法2
        # 后序遍历是 左-右-中 的顺序，反过来就是 中-右-左，这就是二叉树镜像（左右节点互换）的先序遍历顺序。
        # 也就是说，镜像二叉树的先序遍历逆序后就是二叉树后序遍历的顺序。所以在刚才先序遍历的代码基础上，
        # 改一下左右节点入栈顺序，再在最后逆序一下就可以了。
        #    1
        #  2   3
        # 4 5 6 7
        # 镜像之后变成
        #      1
        #   3    2
        # 7  6 5  4
        # 方法1
        stack1 = [root]
        stack2 = []
        while stack1:
            cur = stack1.pop()
            stack2.append(cur.val)
            if cur.left:
                stack1.append(cur.left)
            if cur.right:
                stack1.append(cur.right)
        return stack2[::-1]
        # 方法2
        # if not root:
        #     return []
        # res = []
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         # 注意前序的话是先压右边因为先进后出，所以这里先压左边
        #         res.append(node.val)
        #         stack.append(node.left)
        #         stack.append(node.right)
        # return res[::-1]


Solution().preorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3))))