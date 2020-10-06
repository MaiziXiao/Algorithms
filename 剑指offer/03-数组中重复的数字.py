from typing import List
class Solution:
    """
    找出数组中重复的数字。
    在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，
    也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
    示例 1：

    输入：
    [2, 3, 1, 0, 2, 5, 3]
    输出：2 或 3

    限制：

    2 <= n <= 100000
    """
    def findRepeatNumber(self, nums: List[int]) -> int:
        # # Time performance unacceptable, O(2n)
        # list_seen = []
        # for num in nums:
        #     if num in list_seen:
        #         return num
        #     else:
        #         list_seen.append(num)

        # # Solution 1: time O(n), space O(n) Hash table
        # dict_seen = {}
        # for num in nums:
        #     if num not in dict_seen:
        #         dict_seen[num] = 1
        #     else:
        #         return num

        # # Solution 2: time O(n logn), space O(1) Sort first and check if there is equal neighbours next to each other
        # nums.sort()
        # pre = nums[0]
        # n = len(nums)
        # for index in range(1, n):
        #     if pre == nums[index]:
        #         return pre
        #     pre = nums[index]

        # Solution 3: time O(n), space O(1) loop through the list and put number in the corresponding index
        n = len(nums)
        for i in range(n):
            # While is important since after swap, it still points to the same position
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                else:
                    tmp = nums[i]
                    nums[i], nums[tmp] = nums[tmp], nums[i]
                    # The two lines below are not working. Why?
                    # nums[i] = nums[nums[i]]
                    # nums[nums[i]] = tmp
