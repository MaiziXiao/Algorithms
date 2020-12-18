# 给你一个可装载重量为 W 的背包和 N 个物品，每个物品有重量和价值两个属性。
# 其中第 i 个物品的重量为 wt[i]，价值为 val[i]，现在让你用这个背包装物品，最多能装的价值是多少？
# N = 3, W = 4
# wt = [2, 1, 3]
# val = [4, 2, 3]

# dp[i][j]表示前i件物品体积不超过j的情况下能达到的最大值
# 如果不将物品i放入物品，dp[i][j] = dp[i-1][j]
# 如果放入， dp[i][j] = dp[i-1][j-w]+v

# https://zhuanlan.zhihu.com/p/30959069
from typing import List


def take_items(W: int, weights: List[int], values: List[int]):
    len_weights = W
    len_values = len(values)
    dp = [[0] * (len_weights + 1) for _ in range(len_values + 1)]

    for i in range(1, len_values + 1):
        for j in range(1, len_weights + 1):
            # 如果单个物品重量大过总重，不拿
            if weights[i - 1] > j:
                # 非第一个物品时
                dp[i][j] = dp[i - 1][j]
            # 可以拿的时候,比较拿的value(这个物品的value+减去这个物品重量的最大value)
            # 和不拿哪个高（这个总重量j里目前最大的value）
            else:
                dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]])
    return dp[-1][-1]


take_items(11, [1, 2, 5, 6, 7], [1, 6, 18, 22, 28])
