from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
        如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
        注意：你不能在买入股票前卖出股票。

        示例 1:
        输入: [7,1,5,3,6,4]
        输出: 5
        解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
            注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
        """
        if not prices:
            return 0
        min_val = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] - min_val > max_profit:
                max_profit = prices[i] - min_val
            if prices[i] < min_val:
                min_val = prices[i]

        return max_profit


Solution().maxProfit([7, 1, 5, 3, 6, 4])
