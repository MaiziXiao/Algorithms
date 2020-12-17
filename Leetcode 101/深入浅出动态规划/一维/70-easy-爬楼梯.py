class Solution:
    def climbStairs(self, n: int) -> int:
        """
        假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

        每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

        注意：给定 n 是一个正整数。

        示例 1：
        输入： 2
        输出： 2
        解释： 有两种方法可以爬到楼顶。
        1.  1 阶 + 1 阶
        2.  2 阶

        示例 2：
        输入： 3
        输出： 3
        解释： 有三种方法可以爬到楼顶。
        1.  1 阶 + 1 阶 + 1 阶
        2.  1 阶 + 2 阶
        3.  2 阶 + 1 阶
        """
        d = {}

        def dp(i):
            if not i:
                return 0
            if i == 1 or i == 2:
                return i
            if d.get(i):
                return d[i]
            else:
                d[i] = dp(i - 1) + dp(i - 2)
                return d[i]

        return dp(n)

        # 递归的思想是从后往前，递过去归回来；我们找到了递归公式，也就能写出非递归的实现方式，
        # 当ｎ=1时，有１中走法，当ｎ＝２时，有２种走法；有了这两个基础，就可以求出ｎ＝３时，
        # 有f(n-1) + f(n-2) =3种走法；（也就是斐波那契数列）
        # def climbStairs(self, n):
        #     """
        #     :type n: int
        #     :rtype: int
        #     """
        #     if not n:
        #         return 0
        #     if n == 1 or n == 2:
        #         return n
        #     pre = 2
        #     prepre = 1
        #     ret = 0
        #     for i in range(3, n+1):
        #         ret = pre + prepre
        #         prepre = pre
        #         pre = ret
        #     return ret


Solution().climbStairs(38)
