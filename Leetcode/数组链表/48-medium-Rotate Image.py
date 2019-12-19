from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        You are given an n x n 2D matrix representing an image.
        Rotate the image by 90 degrees (clockwise).

        Note:
        You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
        DO NOT allocate another 2D matrix and do the rotation.

        Example 1:
        Given input matrix =
        [
          [1,2,3],
          [4,5,6],
          [7,8,9]
        ],

        rotate the input matrix in-place such that it becomes:
        [
          [7,4,1],
          [8,5,2],
          [9,6,3]
        ]
        """
        # Own Solution
        n = len(matrix)
        if n == 1:
            return n
        # 圈数
        for i in range(n//2):
            for j in range(i):
                matrix[]
        # Online Solution
        # 先做矩阵转置（即沿着对角线翻转），然后每个列表翻转；
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for m in matrix:
            m.reverse()


Solution().rotate([
          [1,2,3],
          [4,5,6],
          [7,8,9]])
