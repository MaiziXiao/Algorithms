from typing import List
class Solution:
    """
    Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes
    the sum of all numbers along its path.

    Note: You can only move either down or right at any point in time.

    Example:
    Input:
    [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    Output: 7
    Explanation: Because the path 1→3→1→1→1 minimizes the sum.
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        matrix = [[0]*n for _ in range(m)]

        # 第一行第一列赋值
        matrix[0][0] = grid[0][0]
        for i in range(1, n):
            print("i", i)
            matrix[0][i] = matrix[0][i-1] + grid[0][i]
        for i in range(1, m):
            print(i)
            matrix[i][0] = matrix[i-1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1,n):
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1]) + grid[i][j]

        return matrix[m-1][n-1]



Solution().minPathSum([[1,2,5],[3,2,1]])
