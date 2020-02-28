from typing import List

class Solution:
    """
    Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

    Note: The solution set must not contain duplicate subsets.
    Example:
    Input: [1,2,2]
    Output:
    [
      [2],
      [1],
      [1,2,2],
      [2,2],
      [1,2],
      []
    ]
    """
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """回溯法，通过排序参数避免重复排序"""
        # res is the result List
        # tmp 是回溯法中间单个的list
        # k 是现在所在的index
        def DFS(res, tmp, nums, k):
            if tmp not in res:
                res.append(tmp.copy())
            if k == len(nums):
                return
            for i in range(k, len(nums)):
                tmp.append(nums[i])
                DFS(res, tmp, nums, i + 1)
                del tmp[-1]


        nums.sort()
        res = []
        tmp = []
        DFS(res, tmp, nums, 0)
        return res
