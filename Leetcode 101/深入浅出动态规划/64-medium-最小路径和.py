from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

        说明：每次只能向下或者向右移动一步。
        示例 1：


        输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
        输出：7
        解释：因为路径 1→3→1→1→1 的总和最小。
        示例 2：

        输入：grid = [[1,2,3],[4,5,6]]
        输出：12
        """
        result = [[0] * len(grid[0]) for _ in range(len(grid))]
        result[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            result[i][0] = grid[i][0] + result[i - 1][0]
        for i in range(1, len(grid[0])):
            result[0][i] = grid[0][i] + result[0][i - 1]

        for row in range(1, len(grid)):
            for column in range(1, len(grid[0])):
                result[row][column] = min(result[row - 1][column], result[row][column - 1]) + grid[row][column]

        return result[len(grid) - 1][len(grid[0]) - 1]


Solution().minPathSum([[1, 2, 3], [4, 5, 6]])
