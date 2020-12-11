from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。
        规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。
        请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。
        提示:
        输出坐标的顺序不重要
        m 和 n 都小于150
         
        示例：
        给定下面的 5x5 矩阵:

        太平洋 ~   ~   ~   ~   ~
            ~  1   2   2   3  (5) *
            ~  3   2   3  (4) (4) *
            ~  2   4  (5)  3   1  *
            ~ (6) (7)  1   4   5  *
            ~ (5)  1   1   2   4  *
                *   *   *   *   * 大西洋

        返回:

        [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).
        """
        # 使用两个二维数组，分别记录每个位置的点能不能到达太平洋和大西洋。然后对4条边界进行遍历，
        # 看这些以这些边为起点能不能所有的地方。注意了，因为是从边界向中间去寻找，所以，这个时候是新的点要比当前的点海拔高才行。
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        p_visited = [[False] * n for _ in range(m)]
        a_visited = [[False] * n for _ in range(m)]
        for i in range(m):
            # 左边太平洋
            self.dfs(p_visited, matrix, m, n, i, 0)
            # 右边大西洋
            self.dfs(a_visited, matrix, m, n, i, n-1)
        for j in range(n):
            # 上边太平洋
            self.dfs(p_visited, matrix, m, n, 0, j)
            # 下边大西洋
            self.dfs(a_visited, matrix, m, n, m - 1, j)
        res = []
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, visited, matrix, m, n, i, j):
        visited[i][j] = True
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for dire in directions:
            x, y = i + dire[0], j + dire[1]
            # 如果小于前一个，或者超过边界或者已经visit过，不行
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(visited, matrix, m, n, x, y)
