from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 解法1： 使用hash表，一次遍历，时间O(N)，空间O(N)，此方法和leetcode两数之和一样，但那道题数组无序，本题数组有序，所以肯定有更优解
        #
        # 解法2： 使用二分，遍历数组，比如target = 40, nums[0] = 10，那么用二分查找30。时间O(NLogN)，空间O(1)
        #
        # 解法3： 使用双指针，时间O(N) 空间O(1)，应该是最优解了吧。。
        seen = []
        for num in nums:
            if target-num in seen:
                return [num, target-num]
            else:
                seen.append(num)

        # 双指针
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            sum = nums[l] + nums[r]
            if sum == target:
                return [nums[l], nums[r]]
            elif sum > target:
                r -= 1
            else:
                l += 1
        return []