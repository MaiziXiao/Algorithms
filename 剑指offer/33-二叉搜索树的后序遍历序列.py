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
        # 我们都知道BST的中序遍历是有序的，后序遍历时，最后的节点是根节点。那么可以先找根节点，然后利用根节点的值，把数组分成两部分，
        # 前部分都比根节点小是左子树，后部分都比根节点大是右子树。然后再分别遍历左右子树即可。
        # 我做这个题的时候利用从左遍历找到第一个比根节点的大的位置划分左右节点，这样保证了左边部分都比根节点小，不能保证右边部分都比根节点大，所以对右边的部分进行了验证
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

