from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element_count = {}
        length = len(nums)
        if length == 1:
            return nums[0]
        half_length = length//2

        for num in nums:
            if num not in element_count:
                element_count[num] = 1
            else:
                element_count[num] += 1
                if element_count[num] > half_length:
                    return num