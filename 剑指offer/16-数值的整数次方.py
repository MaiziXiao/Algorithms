class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

        示例 1:
        输入: 2.00000, 10
        输出: 1024.00000

        示例 2:
        输入: 2.10000, 3
        输出: 9.26100

        示例 3:
        输入: 2.00000, -2
        输出: 0.25000
        解释: 2-2 = 1/22 = 1/4 = 0.25
        """
        if n == 0:
            return 1
        if n > 0:
            sign = 1
        else:
            sign = -1
        n = n*sign

        res = 1
        while n > 0:
            pow = 1
            pod = x
            while 2*pow < n:
                pow = pow*2
                pod = pod*pod
            n = n-pow
            res = res*pod

        if sign > 0:
            return res
        else:
            return 1/res

print(Solution().myPow(2, -2))