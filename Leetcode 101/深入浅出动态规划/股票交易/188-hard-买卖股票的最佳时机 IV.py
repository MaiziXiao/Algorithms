from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
        设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
        注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

        示例 1：

        输入：k = 2, prices = [2,4,1]
        输出：2
        解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
        """
        if k <= 0 or not prices:
            return 0
        N = len(prices)
        # k 大于N,退化成贪心问题，见122
        # 我们其实可以求至少k次交易的最大利润。我们定义local[i][j]为在到达第i天时最多可进行j次交易
        # 并且最后一次交易在最后一天卖出的最大利润，此为局部最优。然后我们定义global[i][j]为在到达
        # 第i天时最多可进行j次交易的最大利润，此为全局最优。它们的递推式为：

        # local[i][j] = max(global[i - 1][j - 1] + max(diff, 0), local[i - 1][j] + diff)
        # 也就是看两个量，第一个是全局到i-1天进行j-1次交易，然后加上今天的交易，
        # 如果今天是赚钱的话（也就是前面只要j-1次交易，最后一次交易取当前天），
        # 第二个量则是取local第i-1天j次交易，然后加上今天的差值（这里因为local[i-1][j]比如包含第i-1天卖出的交易，
        # 所以现在变成第i天卖出，并不会增加交易次数，而且这里无论diff是不是大于0都一定要加上，
        # 因为否则就不满足local[i][j]必须在最后一天卖出的条件了）。
        # global[i][j] = max(local[i][j], global[i - 1][j])，

        if k >= N:
            _sum = 0
            for i in range(1, N):
                if prices[i] > prices[i - 1]:
                    _sum += prices[i] - prices[i - 1]
            return _sum
        g = [0] * (k + 1)
        local = [0] * (k + 1)
        for i in range(N - 1):
            diff = prices[i + 1] - prices[i]
            for j in range(k, 0, -1):
                local[j] = max(g[j - 1] + max(diff, 0), local[j] + diff)
                g[j] = max(local[j], g[j])
        return g[-1]
