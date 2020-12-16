from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

        两个相邻元素间的距离为 1 。

        示例 1：
        输入：
        [[0,0,0],
        [0,1,0],
        [0,0,0]]

        输出：
        [[0,0,0],
         [0,1,0],
         [0,0,0]]

        示例 2：

        输入：
        [[0,0,0],
        [0,1,0],
        [1,1,1]]

        输出：
        [[0,0,0],
        [0,1,0],
        [1,2,1]]
        """
        # BFS
        q = deque()
        row = len(matrix)
        col = len(matrix[0])
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for x in range(row):
            for y in range(col):
                if matrix[x][y] == 0:
                    q.append((x, y))
                else:
                    # In-place
                    matrix[x][y] = float("inf")
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy
                # matrix[new_x][new_y] > matrix[x][y] + 1 说明matrix[x][y是更短的路径]
                if 0 <= new_x < row and 0 <= new_y < col and matrix[new_x][new_y] > matrix[x][y] + 1:
                    q.append((new_x, new_y))
                    matrix[new_x][new_y] = matrix[x][y] + 1
        return matrix
