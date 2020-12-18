from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

        子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
        例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
        示例 1：

        输入：nums = [10,9,2,5,3,7,101,18]
        输出：4
        解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
        示例 2：

        输入：nums = [0,1,0,3,2,3]
        输出：4
        """
        # Leetcode习惯，子序列（subsequence）一般不必连续，子数组（subarray）或子字符串（substring）必须连续
        # dp[i]是位置i最长递增子序列的长度。
        # 对i来说，和之前所有的j in dp[:i]比，找到最大值
        length = len(nums)
        dp = [1] * (length + 1)
        for i in range(1, length):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

        # 另一种做法就是二分查找法，也很简单，无非就是再新建一个数组，然后第一个数先放进去，然后第二个数和第一个数比较，
        # 如果说大于第一个数，那么就接在他后面，如果小于第一个数，那么就替换，一般的，如果有i个数，那么每进来一个新的数，
        # 都要用二分查找法来得知要替换在哪个位置的数。因为有个for循环，所以是O(N),在加上循环里有个二分查找，所以最后是O(NlogN)的时间复杂度。


Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
