from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

        注意:

        每个数组中的元素不会超过 100
        数组的大小不会超过 200

        示例 1:
        输入: [1, 5, 11, 5]
        输出: true
        解释: 数组可以分割成 [1, 5, 5] 和 [11].
         

        示例 2:
        输入: [1, 2, 3, 5]
        输出: false
        解释: 数组不能分割成两个元素和相等的子集.

        """
        # 背包问题等价问题，取一部分物品，使总和sum/2
        # 首先定义dp数组为dp[i][j]，其意义是使用前i个数字的和能不能构成整数j。
        # 我们需要把每个位置都进行遍历，同时也要对0~target之间的所有正整数进行遍历。
        # 很显然，状态转移的方程是，遍历到i位置时能不能构成target = 前面的数字的和能够成target || 前面的数字能构成target - nums[i]。
        # 这两个状态分别是选不选取nums[i]的两种情况，如果有一种情况成立即可。
        # 状态转移方程如下：
        # dp[i][j] = dp[i - 1][j] || dp[i - 1][j - nums[i]]
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False
        target = sum_nums//2
        dp = [[False]*(target+1) for _ in range(len(nums)+1)]

        for i in range(1, len(nums)+1):
            for j in range(1, target+1):
                if nums[i-1] == j:
                    dp[i][j] = True
                elif nums[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        # 最后一行还可以输出所有可能组成的值
        return dp[-1][-1]


Solution().canPartition([1, 5, 11, 5])
