from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
        影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

        给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

        示例 1：
        输入：[1,2,3,1]
        输出：4
        解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
             偷窃到的最高金额 = 1 + 3 = 4 。

        示例 2：
        输入：[2,7,9,3,1]
        输出：12
        解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
             偷窃到的最高金额 = 2 + 9 + 1 = 12 。
        """
        # d = {}
        # # 假如dfs(i)表示从左到右的第 i 个位置能偷多少金额，
        # # 是不是就是 max(dfs(i - 1), dfs(i - 2) + nums[i])。自顶向下的思路就是递归去求解 dfs(i - 1), dfs(i - 2)。
        # if not nums:
        #     return 0

        # # 在第 i 个房间之前（包括 i）能获取的最大收益
        # def dfs(i):
        #     if i in d:
        #         return d[i]
        #     if i == 0:
        #         res = nums[0]
        #     elif i == 1:
        #         res = max(nums[0], nums[1])
        #     else:
        #         res = max(dfs(i - 1), dfs(i - 2) + nums[i])

        #     d[i] = res
        #     return res

        # return dfs(len(nums) - 1)
        # 非递归
        prev, cur = 0, 0
        for value in nums:
            prev, cur = cur, max(prev + value, cur)
        return cur
