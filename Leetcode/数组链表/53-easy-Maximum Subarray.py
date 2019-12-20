from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

        Example:
        Input: [-2,1,-3,4,-1,2,1,-5,4],
        Output: 6
        Explanation: [4,-1,2,1] has the largest sum = 6.
        Follow up:

        If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
        """
        # O(n) solution
        # 我们定义函数 S(i) ，它的功能是计算以 0（包括 0）开始加到 i（包括 i）的值。
        # 那么 S(j) - S(i - 1) 就等于 从 i 开始（包括 i）加到 j（包括 j）的值
        # 我们进一步分析，实际上我们只需要遍历一次计算出所有的 S(i), 其中 i = 0,1,2....,n-1。
        # 然后我们再减去之前的 S(k),其中 k = 0，1，i - 1，中的最小值即可。 因此我们需要 用一个变量来维护这个最小值，还需要一个变量维护最大值。
        max_sum = nums[0]
        min_sum_from_start = curr_sum = 0
        for i in range(len(nums)):
            curr_sum = curr_sum + nums[i]
            if curr_sum - min_sum_from_start > max_sum:
                max_sum = curr_sum-min_sum_from_start
            if curr_sum < min_sum_from_start:
                min_sum_from_start = curr_sum
        return max_sum

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))