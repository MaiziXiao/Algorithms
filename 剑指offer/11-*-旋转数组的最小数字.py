from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        """
        把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，
        输出旋转数组的最小元素。例如，数组[3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。

        示例 1：
        输入：[3,4,5,1,2]
        输出：1

        示例 2：
        输入：[2,2,2,0,1]
        输出：0
        """
        l, r = 0, len(numbers)-1
        while l < r:
            mid = (r+l)//2
            # 有序在左边，右边找降序最小点
            if numbers[mid] > numbers[r]:
                l = mid+1
            # 有序在右边，左边找降序最小点
            elif numbers[mid] < numbers[r]:
                r = mid
            else:
                r -= 1
        return numbers[l]

Solution().minArray([2,2,2,0,1])