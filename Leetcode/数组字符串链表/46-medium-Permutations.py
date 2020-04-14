from typing import List
class Solution:
    """
    Given a collection of distinct integers, return all possible permutations.

    Example:
    Input: [1,2,3]
    Output:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 排列树, 回溯法
        res = []
        indexs = [x for x in range(len(nums))]
        position = []

        def dfs(indexs):
            if len(position) == len(nums):
                res.append([nums[x] for x in position])

            for index in indexs:
                index_copy = indexs.copy()
                position.append(index)
                index_copy.remove(index)

                dfs(index_copy)

                position.pop()

        dfs(indexs)

        return res


Solution().permute([1,2,3])
