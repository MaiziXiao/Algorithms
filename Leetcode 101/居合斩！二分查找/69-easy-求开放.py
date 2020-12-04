class Solution:
    def mySqrt(self, x: int) -> int:
        """
        实现 int sqrt(int x) 函数。
        计算并返回 x 的平方根，其中 x 是非负整数。
        由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

        示例 1:

        输入: 4
        输出: 2
        """
        left = 1
        right = x
        while left <= right:
            mid = (left + right) // 2
            sqrt = x / mid
            if sqrt == mid:
                return mid
            elif sqrt < mid:
                right = mid - 1
            else:
                left = mid + 1
        return right


Solution().mySqrt(8)
