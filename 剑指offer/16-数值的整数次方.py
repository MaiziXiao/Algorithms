class Solution:
    # def myPow(self, x: float, n: int) -> float:
    #     """
    #     实现函数double Power(double x, int n)，求x的n次方。不得使用库函数，同时不需要考虑大数问题。

    #     示例 1:
    #     输入: 2.00000, 10
    #     输出: 1024.00000

    #     示例 2:
    #     输入: 2.10000, 3
    #     输出: 9.26100

    #     示例 3:
    #     输入: 2.00000, -2
    #     输出: 0.25000
    #     解释: 2-2 = 1/22 = 1/4 = 0.25
    #     """
    #     if n == 0:
    #         return 1
    #     if n > 0:
    #         sign = 1
    #     else:
    #         sign = -1
    #     n = n * sign

    #     res = 1
    #     while n > 0:
    #         pow = 1
    #         pod = x
    #         while 2 * pow < n:
    #             pow = pow * 2
    #             pod = pod * pod
    #         n = n - pow
    #         res = res * pod

    #     if sign > 0:
    #         return res
    #     else:
    #         return 1 / res

    # # 剑指offer解法
    # if x == 0 and n == 0:
    #     return None

    def power(self, base, exponent):
        if base == 0 and exponent == 0:
            return None

        unsigned_exponent = exponent if exponent >= 0 else abs(exponent)

        def unsigned_power(base, unsigned_exponent):
            if unsigned_exponent == 0:
                return 1

            if unsigned_exponent == 1:
                return base

            result = unsigned_power(base, unsigned_exponent >> 1)
            # i.e. 2^32 = 2^16 * 2^16
            result *= result
            # 如果是奇数再乘以自己 2^32 = 2^16 * 2^16 *2
            if unsigned_exponent & 1 == 1:
                result *= base
            return result

        result = unsigned_power(base, unsigned_exponent)
        if exponent < 0:
            return 1.0 / result
        return result


print(Solution().power(2, 32))