class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        """
        0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

        例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

        示例 1：

        输入: n = 5, m = 3
        输出:3
        """
        # 暴力法
        nums = [i for i in range(n)]
        if m == 1:
            return nums[-1]
        count = 1
        i = 0
        while len(nums) > 1:
            if count == m:
                count = 1
                nums.pop(i)
                if i == len(nums):
                    i = 0
                continue
            if i == len(nums)-1:
                count += 1
                i = 0
                continue
            count += 1
            i += 1
        return nums[0]

        # 公式法 https://blog.csdn.net/u011500062/article/details/72855826
        p = 0
        for i in range(2,n+1):
            p = (p + m) % i
        return p
Solution().lastRemaining(5, 1)