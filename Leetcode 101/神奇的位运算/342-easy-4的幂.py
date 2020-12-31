class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。
        整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4^x

        示例 1：
        输入：n = 16
        输出：true

        示例 2：
        输入：n = 5
        输出：false

        示例 3：
        输入：n = 1
        输出：true
        """
        # while n != 0 and n % 4 == 0:
        #     n //= 4
        #     if n == 1:
        #         return True
        # return False

        # https://www.cxyxiaowu.com/6952.html
        # 4的幂次方的二进制在奇数上有1
        # 先判断是否是 2 的幂 (n & (n - 1)) == 0
        return n > 0 and (n & (n - 1)) == 0 and (n & 0b1010101010101010101010101010101) != 0


Solution().isPowerOfFour(16)
