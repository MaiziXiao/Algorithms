class Solution:
    """
    A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
    The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
    How many possible unique paths are there?

    Note: m and n will be at most 100.

    Example 1:
    Input: m = 3, n = 2
    Output: 3
    Explanation:
    From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Right -> Down
    2. Right -> Down -> Right
    3. Down -> Right -> Right

    Example 2:
    Input: m = 7, n = 3
    Output: 28
    """
    def uniquePaths(self, m: int, n: int) -> int:
        # 动态规划 贪心,一个点的总数等于这个点左边那个点总数加上面那个点总数
        # 初始化矩阵
        dp = [[0] * n for _ in range(m)]
        # 第一行和第一列的总数
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[m - 1][n - 1]
