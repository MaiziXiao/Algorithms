from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

        如果数组中不存在目标值 target，返回 [-1, -1]。

        进阶：

        你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
         

        示例 1：

        输入：nums = [5,7,7,8,8,10], target = 8
        输出：[3,4]
        """
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums)-1
        mid = 0
        while left <= right:
            mid = (right + left)//2
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if nums[mid] != target:
            return [-1, -1]
        left, right = mid, mid
        while left > 0 and nums[left-1] == target:
            left -= 1
        while right < len(nums)-1 and nums[right+1] == target:
            right += 1
        return [left, right]
Solution().searchRange([2, 2], 3)