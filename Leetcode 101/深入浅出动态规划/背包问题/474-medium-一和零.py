from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
        请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。
        如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集  

        示例 1：
        输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
        输出：4
        解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
        其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。

        示例 2：
        输入：strs = ["10", "0", "1"], m = 1, n = 1
        输出：2
        解释：最大的子集是 {"0", "1"} ，所以答案是 2 。
        """
        # 这个DP很明白了，定义一个数组dp[m+1][n+1]，代表m个0, n个1能组成的最长字符串。遍历每个字符串统计出现的0和1得到zeros和ones，
        # 所以第dp[i][j]的位置等于dp[i][j]和dp[i - zeros][j - ones] + 1。其中dp[i - zeros][j - ones]表示如果取了当前的这个字符串，那么剩下的可以取的最多的数字。

        # 定义一个3维的dp数组，长度分别为L+1，m+1，n+1，l，m，n分别为string的数量，0的数量和1的数量
        # dp[L][i][j]代表当包含前L个string，并且有i个0，j个1的时候，能形成的string最大数量是多少
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # 三维dp压缩到2维
        for str in strs:
            zeros, ones = 0, 0
            for c in str:
                if c == "0":
                    zeros += 1
                elif c == "1":
                    ones += 1
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[m][n]