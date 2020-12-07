from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        假设按照升序排序的数组在预先未知的某个点上进行了旋转。

        ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

        编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

        示例 1:

        输入: nums = [2,5,6,0,0,1,2], target = 0
        输出: true
        示例 2:

        输入: nums = [2,5,6,0,0,1,2], target = 3
        输出: false"""
        if not nums:
            return False
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            # 如果中点和左端数字相同，无法判断到底是左区间所有数字相同还是有区间所有数字相同
            if nums[mid] == nums[left]:
                left += 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


Solution().search([1, 3, 5], 1)
