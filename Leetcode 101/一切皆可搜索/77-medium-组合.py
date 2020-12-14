from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

        示例:

        输入: n = 4, k = 2
        输出:
        [
        [2,4],
        [3,4],
        [2,3],
        [1,2],
        [1,3],
        [1,4],
        ]
        """
        res = []
        nums = [i + 1 for i in range(n)]

        def dfs(left_nums, cur_list):
            if len(cur_list) == k:
                res.append(cur_list)
                return
            for i in range(len(left_nums)):
                dfs(left_nums[i + 1 :], cur_list + [left_nums[i]])  # noqa:E203

        dfs(nums, [])

        return res


Solution().combine(4, 2)
