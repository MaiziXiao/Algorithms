import math


class Solution:
    def numSquares(self, n: int) -> int:
        """
        给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

        示例 1:

        输入: n = 12
        输出: 3
        解释: 12 = 4 + 4 + 4.
        示例 2:

        输入: n = 13
        输出: 2
        解释: 13 = 4 + 9.
        """
        # dp[i]是数i需要的最少完全平方和
        # dp[i] = min(dp[i-1], dp[i-4], dp[i-9], .....)+1
        dp = [n] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[-1]


Solution().numSquares(8441)
