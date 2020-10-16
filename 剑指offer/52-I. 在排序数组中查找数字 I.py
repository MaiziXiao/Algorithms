from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        统计一个数字在排序数组中出现的次数。
        示例 1:

        输入: nums = [5,7,7,8,8,10], target = 8
        输出: 2
        """
        low = 0
        high = len(nums)-1
        if not nums:
            return 0
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                count = 1
                i = mid - 1
                j = mid + 1
                while i >= 0:
                    if nums[i] == target:
                        count += 1
                        i -= 1
                    else:
                        break
                while j < len(nums):
                    if nums[j] == target:
                        count += 1
                        j += 1
                    else:
                        break
                return count
            if nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return 0

print(Solution().search([1,1,2], 1))
