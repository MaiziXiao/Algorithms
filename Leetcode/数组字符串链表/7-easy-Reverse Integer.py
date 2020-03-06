class Solution:
    """
    Given a 32-bit signed integer, reverse digits of an integer.

    Example 1:
    Input: 123
    Output: 321

    Example 2:
    Input: -123
    Output: -321

    Example 3:
    Input: 120
    Output: 21
    """
    def reverse(self, x: int) -> int:
        res = 0
        sign = -1 if x < 0 else 1
        x = x*sign
        # X 会变0
        while x:
            digit = x % 10
            x = x // 10
            res = res*10 + digit
        # 溢出
        if res > 2147483648 or res < -2147483648:
            return 0
        return sign*res


print(Solution().reverse(10))