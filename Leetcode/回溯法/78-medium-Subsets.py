from typing import List

class Solution:
    """
    Given a set of distinct integers, nums, return all possible subsets (the power set).

    Note: The solution set must not contain duplicate subsets.

    Example:
    Input: nums = [1,2,3]
    Output:
    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Solution 1 深度优先算法回溯
        # def dfs(nums, index, path, res):
        #     """
        #     :param nums: List of the numbers
        #     :param index:
        #     :param path:
        #     :param res:
        #     :return:
        #     """
        #     res.append(path)
        #     for i in range(index, len(nums)):
        #         # 第一轮：先遍历以1开头的所有子集，1→12→123 →13
        #         # 第二轮：遍历以2开头的所有子集，2→23
        #         # 第三轮: 遍历以3开头的所有子集，3
        #         dfs(nums, i + 1, path + [nums[i]], res)
        #
        # res = []
        # nums.sort()
        # dfs(nums, 0, [], res)
        # return res

        # Solution 2 回溯! 是深度搜索的一种 自己写的
        subset_list = []
        subset = []
        def dfs(k):
            """
            :param k: 第 k 个元素
            """
            # 当已经到树最底层的叶支点
            if k == len(nums):
                subset_list.append([nums[k] for k, v in enumerate(subset) if v != 0])  # 保存一个子集, subset is mask
            else:
                for i in range(2):  # 遍历元素 nums[k] 的两种选择状态:1-选择，0-不选
                    subset.append(i)
                    dfs(k + 1)
                    subset.pop()  # 回溯!!!!!!!最重要的一步  把数字pop了以后就可以回上一层
        dfs(0)
        return subset_list

print(Solution().subsets([1,2,3]))