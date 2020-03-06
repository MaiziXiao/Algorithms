from typing import List

class Solution:
    """
    Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.
    Example 1:

    Input:
    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    target = 3
    Output: true
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        height = len(matrix)
        width = len(matrix[0])


        low = 0
        high = height - 1
        mid = 0
        # 看target可能在哪一行,
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target <= matrix[mid][width - 1]:
                break
            if matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1


        possible_row = mid
        low = 0
        high = width - 1
        # 看target是不是在这一行
        while low <= high:
            mid = (low + high) // 2
            if matrix[possible_row][mid] == target:
                return True
            if matrix[possible_row][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 11))