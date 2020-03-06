from typing import List

class Solution:
    """
    Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

    Example:
    Input: 3
    Output:
    [[ 1, 2, 3 ],
     [ 8, 9, 4 ],
     [ 7, 6, 5 ]]
    """
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for j in range(n)]
        nums = [i+1 for i in range(n*n)]

        top = 0
        left = 0
        bottom = n-1
        right = n-1
        while top <= bottom and left <= right:
            for i in range(left, right+1):
                matrix[top][i] = nums.pop(0)
            for i in range(top+1, bottom+1):
                matrix[i][right] = nums.pop(0)
            for i in range(right-1, left, -1):
                matrix[bottom][i] = nums.pop(0)
            for i in range(bottom, top, -1):
                matrix[i][left] = nums.pop(0)
            left += 1
            top += 1
            right -= 1
            bottom -= 1

        return matrix

print(Solution().generateMatrix(3))