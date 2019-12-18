from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
        Your algorithm's runtime complexity must be in the order of O(log n).
        If the target is not found in the array, return [-1, -1].

        Example 1:
        Input: nums = [5,7,7,8,8,10], target = 8
        Output: [3,4]

        Example 2:
        Input: nums = [5,7,7,8,8,10], target = 6
        Output: [-1,-1]
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] == target:
                low_index = mid
                high_index = mid
                # 从找到的数开始分别向左右开始找
                # Own Solution
                # i = 1
                # while i <= len(nums):
                #     if mid-i >= 0 and nums[mid-i] == target:
                #         low_index = mid - i
                #     if mid+i <= len(nums)-1 and nums[mid+i] == target:
                #         high_index = mid + i
                #     i += 1

                # Online Solution
                while target == nums[low_index - 1] and low_index > 0:
                    low_index -= 1
                while high_index < len(nums) - 1 and target == nums[high_index + 1]:
                    high_index += 1
                return [low_index, high_index]
        return [-1, -1]

result = Solution().searchRange([3,3,3], 3)
print(result)