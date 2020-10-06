from typing import List
class Solution:
    """
    Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

    Example:

    Input: n = 4, k = 2
    Output:
    [
      [2,4],
      [3,4],
      [2,3],
      [1,2],
      [1,3],
      [1,4],
    ]
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        cur = []
        nums = [i+1 for i in range(n)]

        def dfs(nums, cur):
            if len(cur) == k:
                res.append(cur)

            for i in range(len(nums)):
                dfs(nums[i+1:], cur+[nums[i]])

        dfs(nums, cur)
        return res

print(Solution().combine(4, 2))