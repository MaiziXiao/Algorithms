from typing import List
import random
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

        示例 1:

        输入: [3,2,1,5,6,4] 和 k = 2
        输出: 5
        示例 2:

        输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
        输出: 4
        """
        # 快速选择一般用于求解k-th element问题，可以在O(n)时间,O(1)空间复杂度完成求解， 和快速排序算法思路很像
        # Quick Select, 利用快排的partition函数思想，选定一个数组内的值作为pivot，将小于pivot的数字放到pivot右边，大于等于pivot的数字放到pivot左边。
        # 接着判断两边数字的数量，如果左边的数量小于k个，说明第k大的数字存在于pivot及pivot右边的区域之内，对右半区执行partition函数；如果右边的数量小于k个，
        # 说明第k大的数字在pivot和pivot左边的区域之内，对左半区执行partition函数。直到左半区刚好有k-1个数，那么第k大的数就已经找到了。
        pivot = random.choice(nums)
        nums1, nums2 = [], []
        for num in nums:
            if num > pivot:
                nums1.append(num)
            elif num < pivot:
                nums2.append(num)
        # k在右边的nums1
        if k <= len(nums1):
            return self.findKthLargest(nums1, k)
        # len(nums) - len(nums2)等于大于等于pivot的数量
        elif k > len(nums) - len(nums2):
            # 所有比pivot小里的第k - (len(nums) - len(nums2))个
            return self.findKthLargest(nums2, k - (len(nums) - len(nums2)))
        else:
            return pivot

        # 堆排序
        # https://blog.csdn.net/XX_123_1_RJ/article/details/80819850
        def findKthLargest(self, nums, k):
            return heapq.nlargest(k, nums)[-1]


Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
