from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        """
        输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回true，否则返回false。假设输入的数组的任意两个数字都互不相同。

        参考以下这颗二叉搜索树：

             5
            / \
           2   6
          / \
         1   3

        示例 1：
        输入: [1,6,3,2,5]
        输出: false

        示例 2：
        输入: [1,3,2,6,5]
        输出: true
        """
        # 二叉搜索树即是二叉排序树，
        # 1. 后序遍历序列的最后一个元素为二叉树的根节点；
        # 2. 二叉搜索树左子树上所有的结点均小于根结点、右子树所有的结点均大于根结点。
        # 算法步骤如下：
        # 1. 找到根结点；
        # 2. 遍历序列，找到第一个大于等于根结点的元素i，则i左侧为左子树、i右侧为右子树；
        # 3. 我们已经知道i左侧所有元素均小于根结点，那么再依次遍历右侧，看是否所有元素均大于根结点；若出现小于根结点的元素，则直接返回false；
        # 若右侧全都大于根结点，则：
        # 4. 分别递归判断左/右子序列是否为后序序列；
        if len(postorder) == 1 or len(postorder) == 2:
            return True
        heap = []
        while postorder:
            print(heap, postorder)
            if len(heap) >= 2:
                if heap[-2] < postorder[0] < heap[-1]:
                    heap.pop(-2)
                    heap.pop(-1)
            heap.append(postorder.pop(0))
        print(heap)
        if len(heap) == 1:
            return True
        else:
            return False

Solution().verifyPostorder([4, 6, 7, 5])

