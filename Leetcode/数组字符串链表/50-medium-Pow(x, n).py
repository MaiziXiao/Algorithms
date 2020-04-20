class Solution:
    """
    Implement pow(x, n), which calculates x raised to the power n (xn).

    Example 1:
    Input: 2.00000, 10
    Output: 1024.00000

    Example 2:
    Input: 2.10000, 3
    Output: 9.26100

    Example 3:
    Input: 2.00000, -2
    Output: 0.25000
    Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25

    Note:
    -100.0 < x < 100.0
    n is a 32-bit signed integer, within the range [−231, 231 − 1]
    """
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -1*n

        res = 1

        while n > 0:
            num = 1
            base = x
            # 二分法
            while 2*num < n:
                num = num*2
                base = base**2
            res *= base
            n -= num

        return res


print(Solution().myPow(2,-10))