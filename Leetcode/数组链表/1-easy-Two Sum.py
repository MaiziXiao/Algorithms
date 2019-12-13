import itertools


class Solution(object):
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 1. one pass hash-table
        # lookup = {}
        # for i, num in enumerate(nums):
        #     if target - num in lookup:
        #         return [lookup[target - num], i]
        #     lookup[num] = i
        # return []

        # 2. brute force (own solution)
        for a, b in itertools.combinations(enumerate(nums), 2):
            if a[1] + b[1] == target:
                return [a[0], b[0]]

        # 3. brute force (online solution)
        # k = 0
        # for i in nums:
        #     j = target - i
        #     k += 1
        #     tmp_nums = nums[k:]
        #     if j in tmp_nums:
        #         return [k - 1, tmp_nums.index(j) + k]


nums1 = [3, 2, 5, 1]
target1 = 6
solution = Solution()
print(solution.twoSum(nums1,target1))