from typing import List


class Solution:
    """
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
    (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
    You are given a target value to search. If found in the array return true, otherwise return false.

    Example 1:
    Input: nums = [2,5,6,0,0,1,2], target = 0
    Output: true
    """
    def search(self, nums: List[int], target: int) -> bool:
        low = 0
        high = len(nums) - 1
        while low <= high:
            # 33题的变种,是加了一个可能含有重复数字。
            # 这样的话，如果直接进行左右指针的比较就不知道向哪个方向搜索了，所以，需要在正式比较之前，先移动左指针，
            # 使他指向一个和右指针不同的数字上。然后再做33题的查找。
            while low < high and nums[low] == nums[high]:
                low += 1
            mid = (low + high)//2
            print(low, mid, high)
            if target == nums[mid]:
                return True
            if target == nums[low]:
                return True
            if target == nums[high]:
                return True
            # 有序部分在左边
            if nums[mid] >= nums[low]:
                if nums[low] < target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # 有序部分在右边
            else:
                if nums[mid] < target < nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False

print(Solution().search([1,1,3,1], 3))