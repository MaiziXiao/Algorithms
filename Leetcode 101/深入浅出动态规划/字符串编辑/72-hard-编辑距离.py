class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

        你可以对一个单词进行如下三种操作：

        插入一个字符
        删除一个字符
        替换一个字符


        示例 1：

        输入：word1 = "horse", word2 = "ros"
        输出：3
        解释：
        horse -> rorse (将 'h' 替换为 'r')
        rorse -> rose (删除 'r')
        rose -> ros (删除 'e')
        """
        # dp[i][j] 第一个字符串到i为止，和第二个字符串到j为止，最多需要几步编辑
        # 如果相等，则最后一个字符不用做任何操作，那么只用计算除去最后一个字符外的前面的子串的编辑距离即可。word1[i] == word2[j]，dp[i][j] = dp[i-1][j-1]
        # 如果不等，则最后一个字符需要进行替换操作，那么只用计算除去最后一个字符外的前面的子串的编辑距离 ，再 +1（最后一个字符的替换操作），
        # 即可把word1变成word2。
        L1, L2 = len(word1), len(word2)
        dp = [[0] * (L2 + 1) for _ in range(L1 + 1)]
        for i in range(L1 + 1):
            dp[i][0] = i
        for j in range(L2 + 1):
            dp[0][j] = j
        for i in range(1, L1 + 1):
            for j in range(1, L2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[L1][L2]
