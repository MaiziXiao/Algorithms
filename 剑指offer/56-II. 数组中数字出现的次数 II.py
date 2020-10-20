from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
        """

        # 如果一个数字出现3次，它的二进制每一位也出现的3次。如果把所有的出现三次的数字的二进制表示的每一位都分别加起来，那么每一位都能被3整除。
        # 我们把数组中所有的数字的二进制表示的每一位都加起来。如果某一位能被3整除，那么这一位对只出现一次的那个数的这一肯定为0。
        # 如果某一位不能被3整除，那么只出现一次的那个数字的该位置一定为1.
        ans = 0
        # 分别检测ans的各个位
        for i in range(32):
            count = 0
            # 如果nums所有的num中第i位不能被3整除，证明ans的第i位为1
            for num in nums:
                count += num & (1 << i)
            # ans的第i位置1
            if count % 3:
                ans += (1 << i)
        return ans