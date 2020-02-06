from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
    Example 1:
    Input:
    [
      [1,1,1],
      [1,0,1],
      [1,1,1]
    ]
    Output:
    [
      [1,0,1],
      [0,0,0],
      [1,0,1]
    ]
        """
        m = len(matrix)
        n = len(matrix[0])

        first_row_has_zero = False
        first_column_has_zero = False
        # 第一行有0吗
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break

        # 第一列有0吗
        for i in range(m):
            if matrix[i][0] == 0:
                first_column_has_zero = True
                break

        # 如果出现0,把这一行和列的第一个元素变成0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 看第一列,如果有0就更新一行
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        # 看第一行,如果有0就更新一列
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # 更新第一行第一列
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_column_has_zero:
            for i in range(m):
                matrix[i][0] = 0
