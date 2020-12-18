# 1.1. 最长公共子序列（Longest-Common-Subsequences，LCS）
# 最长公共子序列（Longest-Common-Subsequences，LCS）是一个在一个序列集合中（通常为两个序列）用来查找所有序列中最长子序列的问题。这与查找最长公共子串的问题不同的地方是：子序列不需要在原序列中占用连续的位置 。

# 最长公共子序列问题是一个经典的计算机科学问题，也是数据比较程序，比如Diff工具，和生物信息学应用的基础。它也被广泛地应用在版本控制，比如Git用来调和文件之间的改变。

# 1.2 最长公共子串（Longest-Common-Substring，LCS）
# 最长公共子串（Longest-Common-Substring，LCS）问题是寻找两个或多个已知字符串最长的子串。此问题与最长公共子序列问题的区别在于子序列不必是连续的，而子串却必须是连续的。


class Solution:
    def longestCommonString(self, X: str, Y: str) -> str:

        # 在最长公共子序列中，dp[i][j]表示str_a[1:i]和str_b[1:j]的最长公共子序列，是从str_a的1和str_b的1开始计算的，即整个字符串的起始位置。
        # 在最长公共子串中，dp[i][j]表示str_a[i':i]和str_b[j':j]的最长公共子串，因为str_a和str_b可能存在多个公共子串，所以i'和j'分别表示当前公共子串的起始位置。
        # 也就是说：

        # 当str_a[i] == str_b[j]时，dp[i][j] = dp[i-1][j-1]+ 1；
        # 当str_a[i] != str_b[j]时，dp[i][j] = 0，即开始计算新的公共子串。
        m = len(X)
        n = len(Y)
        LCSuff = [[0 for k in range(n + 1)] for _ in range(m + 1)]

        # To store the length of
        # longest common substring
        result = 0

        # Following steps to build
        # LCSuff[m+1][n+1] in bottom up fashion
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 当str_a[i] == str_b[j]时，dp[i][j] = dp[i-1][j-1]+ 1；
                # 当str_a[i] != str_b[j]时，dp[i][j] = 0，即开始计算新的公共子串。
                if X[i - 1] == Y[j - 1]:
                    LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1
                    result = max(result, LCSuff[i][j])
        return result


Solution().longestCommonString("abcdxyda", "abcfxyda")
