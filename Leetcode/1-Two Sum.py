import itertools
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
#one pass hash-table
        # lookup = {}
        # for i, num in enumerate(nums):
        #     if target - num in lookup:
        #         return [lookup[target - num], i]
        #     lookup[num] = i
        # return []
#brute force
        #own solution
        for a,b in itertools.combinations(enumerate(nums), 2):
            if a[1] + b[1] == target:
                return [a[0], b[0]]
        #online
        # k = 0
        # for i in nums:
        #     j = target - i
        #     k += 1
        #     tmp_nums = nums[k:]
        #     if j in tmp_nums:
        #         return [k - 1, tmp_nums.index(j) + k]
nums1 = [3,3]
target1 = 6
solution = Solution()
print(solution.twoSum(nums1,target1))