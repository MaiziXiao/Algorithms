from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

        说明：

        初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
        你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
         

        示例：

        输入：
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6],       n = 3

        输出：[1,2,2,3,5,6]
        Do not return anything, modify nums1 in-place instead.
        """
        # 这里要求原地修改，其实我们能只要从后往前比较，并从后往前插入即可。
        while m > 0 and n > 0:
            if nums1[m-1] <= nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
        # 由于没有使用 current，第一步比较结束后有两种情况:
        #     1. 指针 m>0，n=0，此时不需要做任何处理
        #     2. 指针 n>0，m=0，此时需要将 nums2 指针左侧元素全部拷贝到 nums1 的前 n 位
        if n > 0:
            nums1[:n] = nums2[:n]


Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
