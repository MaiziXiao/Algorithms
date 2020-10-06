from typing import List
class Solution:
    """
    Given a collection of numbers that might contain duplicates, return all possible unique permutations.

    Example:
    Input: [1,1,2]
    Output:
    [
      [1,1,2],
      [1,2,1],
      [2,1,1]
    ]
    """
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums, path):
            if len(nums) == 0:
                res.append(path)
                return
            for i in range(len(nums)):
                # 和前一个一样的时候直接跳过深度搜索
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                # 不一样的时候往深搜, 把i给排除
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]])

        nums.sort()
        res = []
        dfs(nums, [])

        return res


print(Solution().permute([1,2,1]))
