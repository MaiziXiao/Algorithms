from typing import List

class Solution:
    """
    Given an array of non-negative integers, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position.
    Determine if you are able to reach the last index.

    Example 1
    Input: [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

    Example 2:
    Input: [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum
                 jump length is 0, which makes it impossible to reach the last index.
    """
    def canJump(self, nums: List[int]) -> bool:
        # https://leetcode.com/articles/jump-game/
        # Approach 1: 贪心算法
        _max = 0
        _len = len(nums)
        for i in range(_len-1):
            if i == len(nums) - 1:
                return True
            # 根本到不了这步
            if _max < i:
                return False
            # 更新max: 判断max和现在这个位置能跳到最远的位置谁大
            _max = max(_max, nums[i] + i)
        return _max >= _len - 1

        # Approach 2: 回溯 backtracking
        # This is the inefficient solution where we try every single jump pattern that takes us from the first
        # position to the last. We start from the first position and jump to every index that is reachable.
        # We repeat the process until last index is reached. When stuck, backtrack.

        # Approach 3: 动态规划

print(Solution().canJump([2,5,0,0]))