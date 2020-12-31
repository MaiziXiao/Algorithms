from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        """
        给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

        示例 1:
        输入: 2
        输出: [0,1,1]

        示例 2:
        输入: 5
        输出: [0,1,1,2,1,2]
        """
        #    0000    0
        #     -------------
        #     0001    1
        #     -------------
        #     0010    1
        #     0011    2
        #     -------------
        #     0100    1
        #     0101    2
        #     0110    2
        #     0111    3
        #     -------------
        #     1000    1
        #     1001    2
        #     1010    2
        #     1011    3
        #     1100    2
        #     1101    3
        #     1110    3
        #     1111    4
        # 如果最后一位是1，dp[i] = dp[i-1] +1
        # 如果是0，比如dp[0b1100], dp[0b1100] = dp[0b0110], dp[i] = dp[i>>1]
        if not num:
            return [0]
        dp = [0] * (num + 1)
        dp[1] = 1
        for i in range(2, num + 1):
            if i % 2 == 1:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i >> 1]
        return dp


Solution().countBits(5)