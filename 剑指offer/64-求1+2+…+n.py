class Solution:
    def sumNums(self, n: int) -> int:
        """
        求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
        """
        # return sum(list(range(1, 1 + n)))
        # 要注意 Python 中逻辑运算符的用法，例如 a and b 的情况：a 为 False，返回 a；a 为 True，就返回 b。
        # 并且 and 的左右两边是不能执行赋值运算操作的
        # 当n = 0的时候a为0时，返回0，不会继续递归下去
        return (n and n + self.sumNums(n - 1))