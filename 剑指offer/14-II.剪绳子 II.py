class Solution:
    def cuttingRope(self, n: int) -> int:
        # https://zhuanlan.zhihu.com/p/151037922
        MOD = 1000000007
        if n <= 3:
            return n - 1
        if n % 3 == 0:
            # 恰好被3整除
            return 3 ** (n//3) % MOD
        elif n % 3 == 1:
            # 余数为1, 转成2*2
            return 3 ** (n//3-1) * 2 * 2 % MOD
        else:
            # 余数为2, 直接乘以最后一个2
            return 3 ** (n//3) * 2 % MOD