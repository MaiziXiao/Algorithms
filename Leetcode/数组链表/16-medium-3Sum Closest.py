class Solution:
    """
    Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to
    target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    Example:
    Given array nums = [-1, 2, 1, -4], and target = 1.
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
    """
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        result = nums[0] + nums[1] + nums[2]
        for index_1 in range(n - 2):
            # 很重要，不尝试重复的数字
            if index_1 > 0 and nums[index_1] == nums[index_1-1]:
                continue
            index_2 = index_1 + 1
            index_3 = n - 1
            while index_2 < index_3:
                current_sum = nums[index_1] + nums[index_2] + nums[index_3]
                if abs(current_sum - target) == 0:
                    return target
                # 不用更新index，下一个while循环不满足小于(因为等于)，会调到下一个if判断
                elif abs(current_sum - target) < abs(result - target):
                    result = current_sum
                elif current_sum < target:
                    index_2 += 1
                else:
                    index_3 -= 1
        return result


print(Solution().threeSumClosest([1,2,5,10,11], 12))
