class Solution:
    def __init__(self):
        self.dict = {0: 0, 1: 1}
    def fib(self, n: int) -> int:
        """
        写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

        F(0) = 0,   F(1) = 1
        F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
        斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

        答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

        示例 1：
        输入：n = 2
        输出：1

        示例 2：
        输入：n = 5
        输出：5
        """
        # https://zhuanlan.zhihu.com/p/56444434
        # 1.递归 时间复杂度O(n), 如果不用字典复杂度O(2^n)
        # !小心，dict初始化在class init里不在函数里
        if n in self.dict:
            return self.dict[n]
        else:
            a = (self.fib(n-1) + self.fib(n-2))%1000000007
            self.dict[n] = a
            return a

        # 2.循环 时间复杂度O(n)
        if n <= 1:
            return n
        a, b = 0, 1
        while n > 0:
            a, b = b, a + b
            n -= 1
        return a


print(Solution().fib(45))
