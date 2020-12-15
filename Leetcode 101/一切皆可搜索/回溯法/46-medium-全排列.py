from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        给定一个 没有重复 数字的序列，返回其所有可能的全排列。

        示例:

        输入: [1,2,3]
        输出:
        [
        [1,2,3],
        [1,3,2],
        [2,1,3],
        [2,3,1],
        [3,1,2],
        [3,2,1]
        ]
        """
        res = []

        def dfs(left_nums, cur_list):
            if len(cur_list) == len(nums):
                res.append(cur_list)
            for i in range(len(left_nums)):
                dfs(left_nums[:i] + left_nums[i + 1:], cur_list + [left_nums[i]])

        dfs(nums, [])
        return res

        # 如果右重复
        # def dfs(nums, path):
        #     if len(nums) == 0:
        #         res.append(path)
        #         return
        #     for i in range(len(nums)):
        #         # 和前一个一样的时候直接跳过深度搜索
        #         if i > 0 and nums[i] == nums[i - 1]:
        #             continue
        #         # 不一样的时候往深搜, 把i给排除
        #         dfs(nums[:i] + nums[i + 1:], path + [nums[i]])

        # nums.sort()
        # res = []
        # dfs(nums, [])

        # return res


print(Solution().permute([1, 2, 3]))
