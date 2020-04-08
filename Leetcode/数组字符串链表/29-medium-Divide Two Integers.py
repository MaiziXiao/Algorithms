class Solution:
    """
    Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

    Return the quotient after dividing dividend by divisor.

    The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

    Example 1:
    Input: dividend = 10, divisor = 3
    Output: 3
    Explanation: 10/3 = truncate(3.33333..) = 3.

    Example 2:
    Input: dividend = 7, divisor = -3
    Output: -2
    Explanation: 7/-3 = truncate(-2.33333..) = -2.

    Note:
    Both dividend and divisor will be 32-bit signed integers.
    The divisor will never be 0.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
    [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
    """
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0 ):
            sign = 1
        else:
            sign = -1

        res = 0
        a = abs(dividend)
        b = abs(divisor)
        sum = 0
        count = 0

        # 二分法
        while a >= b:
            sum = b
            count = 1
            # 斐波那契数列 1,2,3,5,8,
            while sum + sum <= a:
                sum += sum
                count += count
            a -= sum
            res += count

        res = res*sign
        if -2**31 <= res <= 2**31-1:
            return res
        else:
            return 2**31-1

