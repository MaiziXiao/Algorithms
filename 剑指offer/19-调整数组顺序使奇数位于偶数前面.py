from typing import List
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        """
        输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

        示例：
        输入：nums = [1,2,3,4]
        输出：[1,3,2,4]
        注：[3,1,2,4] 也是正确的答案之一。
        """
        # 时间复杂度O(n)，空间复杂度O(1)
        end = 0
        for i in range(len(nums)):
            num = nums[i-end]
            # 偶数
            if num % 2 == 0:
                nums.append(num)
                nums.pop(i-end)
                end += 1
            # 奇数不用操作
        return nums

print(Solution().exchange([2,16,3,5,13,1,16,1,12,18,11,8,11,11,5,1]))