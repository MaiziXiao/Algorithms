from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Given a sorted array and a target value, return the index if the target is found. If not, return the index where
        it would be if it were inserted in order. You may assume no duplicates in the array.

        Example 1:
        Input: [1,3,5,6], 5
        Output: 2

        Example 2:
        Input: [1,3,5,6], 2
        Output: 1
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low+high) // 2
            print(low, mid, high)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high -= 1
            elif nums[mid] < target:
                low += 1
        # 最后low mid high会变成一个数
        if nums[mid] > target:
            return mid
        else:
            return mid + 1


print(Solution().searchInsert([1,3,5,6], 7)) # [1,3,5,6], 7