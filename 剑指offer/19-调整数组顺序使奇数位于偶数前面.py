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
            num = nums[i - end]
            # 偶数
            if num % 2 == 0:
                nums.append(num)
                nums.pop(i - end)
                end += 1
            # 奇数不用操作
        return nums

        def reorder(nums, target_func):
            # 双指针
            if not isinstance(nums, list) or len(nums) == 0:
                return

            for num in nums:
                if not isinstance(num, int):
                    return

            left = 0
            right = len(nums) - 1
            while left < right:
                # left奇数 l +=1
                while left < right and not (nums[right] & 1) == 0:
                    left += 1

                while left < right and (nums[right] & 1):
                    # right 偶数 r -= 1
                    right -= 1
                # left 偶，right奇，换
                if left < right:
                    nums[left], nums[right] = nums[right], nums[left]


print(Solution().exchange([2, 16, 3, 5, 13, 1, 16, 1, 12, 18, 11, 8, 11, 11, 5, 1]))
