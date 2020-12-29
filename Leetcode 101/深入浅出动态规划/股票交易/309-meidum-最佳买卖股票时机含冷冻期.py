from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
        设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
        你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
        卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

        示例:
        输入: [1,2,3,0,2]
        输出: 3
        解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
        """
        # 两个状态 sell和hold
        # sell 该天结束手里没有股票的情况下，已经获得的最大收益
        # hold 该天结束手里有股票的情况下，已经获得的最大收益
        # 状态转移方程式这样的：

        # sell[i]代表的是手里没有股票的收益，这种可能性是今天卖了或者啥也没干。
        # max(昨天手里有股票的收益+今天卖股票的收益，昨天手里没有股票的收益)， 即max(sell[i - 1], hold[i - 1] + prices[i])；

        # hold[i]代表的是手里有股票的收益，这种可能性是今天买了股票或者啥也没干，
        # 今天买股票必须昨天休息。所以为max(今天买股票是前天卖掉股票的收益-今天股票的价格，昨天手里有股票的收益）。
        # 即max(hold[i - 1], sell[i - 2] - prices[i])。

        # 该算法的时间复杂度是O(n)，空间复杂度是O(n)。
        sell = [0] * len(prices)
        hold = [0] * len(prices)
        hold[0] = -prices[0]
        for i in range(1, len(prices)):
            sell[i] = max(sell[i - 1], hold[i - 1] + prices[i])
            hold[i] = max(hold[i - 1], (sell[i - 2] if i >= 2 else 0) - prices[i])
        return sell[-1]
