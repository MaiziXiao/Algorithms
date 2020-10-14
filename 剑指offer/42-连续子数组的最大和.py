from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

        要求时间复杂度为O(n)。

        示例1:

        输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
        输出: 6
        解释:连续子数组[4,-1,2,1] 的和最大，为6。
        """
        # Go through the list, save the minimum s(i),compare s(j) - s(i) with maxnum
        min_sum = 0
        cur_sum = 0
        max_sum = nums[0]
        for num in nums:
            cur = cur+num
            max_sum = max(max_sum, cur-min_sum)
            min_sum = min(min_sum, cur)
        return max_sum