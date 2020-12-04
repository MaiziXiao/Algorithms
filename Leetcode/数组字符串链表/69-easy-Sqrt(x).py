class Solution:
    """
    Implement int sqrt(int x).

    Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

    Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

    Example 1:
    Input: 4
    Output: 2

    Example 2:
    Input: 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since
                 the decimal part is truncated, 2 is returned.
    """

    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left = 1
        right = x

        while left <= right:
            mid = (left + right) // 2
            print(left, mid, right)
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            elif (mid + 1) ** 2 == x:
                return mid + 1
            elif x < mid ** 2:
                right = mid - 1
            elif (mid + 1) ** 2 < x:
                left = mid + 1


print(Solution().mySqrt(2147395599))