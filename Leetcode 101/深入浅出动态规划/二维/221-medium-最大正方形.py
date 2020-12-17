from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

        示例 1：


        输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
        输出：4
        """

        if not matrix:
            return 0
        M = len(matrix)
        N = len(matrix[0])
        # dp[i][j]以(i,j)为右下角最大的正方形面积
        dp = [[0] * N for _ in range(M)]
        for i in range(M):
            dp[i][0] = int(matrix[i][0])
        for j in range(N):
            dp[0][j] = int(matrix[0][j])
        for i in range(1, M):
            for j in range(1, N):
                if int(matrix[i][j]) == 1:
                    # i.e.如果左边左上上都是可以有最大2的正方形，那么右下最大可以3
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                # 如果不是1就是default的0
        return max(map(max, dp)) ** 2