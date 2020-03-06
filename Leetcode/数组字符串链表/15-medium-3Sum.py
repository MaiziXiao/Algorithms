class Solution:
    """
    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique
    triplets in the array which gives the sum of zero.
    Note:
    The solution set must not contain duplicate triplets.

    Example:
    Given array nums = [-1, 0, 1, 2, -1, -4],
    A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]
    """
    def threeSum(self, nums):
        # Own solution
        nums.sort()
        final_list = set()
        for index_1 in range(len(nums)-2):
            # 两个指针从左右向中间
            index_2 = index_1 + 1
            index_3 = len(nums) - 1
            # 如果左边不是相同值[1 ,1, X, X, X]
            if index_1 > 0 and nums[index_1] == nums[index_1 - 1]:
                continue
            while index_2 < index_3:
                if nums[index_2] + nums[index_3] == -1 * nums[index_1]:
                    final_list.add(tuple(sorted([nums[index_1], nums[index_2], nums[index_3]])))
                    index_2 += 1
                    # while index_2 < index_3 and nums[index_2] == nums[index_3]:
                    #     index_2 += 1
                elif nums[index_2] + nums[index_3] <= -1 * nums[index_1]:
                    index_2 += 1
                else:
                    index_3 -= 1
        return final_list


print(Solution().threeSum([1, -1, 0, 3, 5]))








