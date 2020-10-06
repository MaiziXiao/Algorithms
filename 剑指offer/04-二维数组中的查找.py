from typing import List
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        """
        在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
        请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
        示例:

        现有矩阵 matrix 如下：

        [
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
        ]
        给定 target = 5，返回 true。

        给定 target = 20，返回 false。

        限制：

        0 <= n <= 1000
        0 <= m <= 1000
        """
        # 从右上角看，就是一个二叉树
        # # 1. 循环
        # if not matrix:
        #     return False
        # m = len(matrix)
        # n = len(matrix[0])
        #
        # row = 0
        # column = n
        # while row < m and column > 0:
        #     if matrix[row][column-1] == target:
        #         return True
        #     elif matrix[row][column-1] < target:
        #         row += 1
        #     else:
        #         column -= 1
        # return False

        # 2. 递归
        self.result = False
        if not matrix:
            return False
        def find(m, n):
            if m >= len(matrix) or n < 0:
                return
            elif matrix[m][n] == target:
                self.result = True
            elif matrix[m][n] > target:
                find(m, n - 1)
            else:
                find(m + 1, n)

        find(0, len(matrix[0])-1)

        return self.result
