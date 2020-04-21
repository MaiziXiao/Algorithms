from typing import List

class Solution:
    """
    A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
    The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right
    corner of the grid (marked 'Finish' in the diagram below).
    An obstacle and empty space is marked as 1 and 0 respectively in the grid.

    Example 1:
    Input:
    [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]
    Output: 2

    Explanation:
    There is one obstacle in the middle of the 3x3 grid above.
    There are two ways to reach the bottom-right corner:
    1. Right -> Right -> Down -> Down
    2. Down -> Down -> Right -> Right
    """
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid) # height
        m = len(obstacleGrid[0]) # width
        final_grid = [[0] * m for _ in range(n)]

        if obstacleGrid[0][0] != 1:
            final_grid[0][0] = 1

        # Initialize the first row and column
        for i in range(1,m):
            # Left grid is not obstacle
            if obstacleGrid[0][i-1] != 1 and obstacleGrid[0][i] != 1:
                final_grid[0][i] = final_grid[0][i-1]
            else:
                final_grid[0][i] = 0

        for i in range(1, n):
            # Upper grid and itself is not obstacle
            if obstacleGrid[i-1][0] != 1 and obstacleGrid[i][0] != 1:
                final_grid[i][0] = final_grid[i-1][0]
            else:
                final_grid[i][0] = 0

        for j in range(1,m):
            for i in range(1,n):
                print(i, j)
                if obstacleGrid[i][j] == 1:
                    final_grid[i][j] == 0
                    continue
                final_grid[i][j] = final_grid[i][j-1]*(1-obstacleGrid[i][j-1]) + final_grid[i-1][j]*(1-obstacleGrid[i-1][j])
        return final_grid[n-1][m-1]


Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])

