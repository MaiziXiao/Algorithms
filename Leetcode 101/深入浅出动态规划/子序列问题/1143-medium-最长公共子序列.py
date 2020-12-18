# 1.1. 最长公共子序列（Longest-Common-Subsequences，LCS）
# 最长公共子序列（Longest-Common-Subsequences，LCS）是一个在一个序列集合中（通常为两个序列）
# 用来查找所有序列中最长子序列的问题。这与查找最长公共子串的问题不同的地方是：子序列不需要在原序列中占用连续的位置 。

# 最长公共子序列问题是一个经典的计算机科学问题，也是数据比较程序，比如Diff工具，和生物信息学应用的基础。
# 它也被广泛地应用在版本控制，比如Git用来调和文件之间的改变。

# 1.2 最长公共子串（Longest-Common-Substring，LCS）
# 最长公共子串（Longest-Common-Substring，LCS）问题是寻找两个或多个已知字符串最长的子串。
# 此问题与最长公共子序列问题的区别在于子序列不必是连续的，而子串却必须是连续的。


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

        一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符
        （也可以不删除任何字符）后组成的新字符串。
        例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

        若这两个字符串没有公共子序列，则返回 0。

         

        示例 1:
        输入：text1 = "abcde", text2 = "ace"
        输出：3
        解释：最长公共子序列是 "ace"，它的长度为 3

        示例 2:
        输入：text1 = "abc", text2 = "abc"
        输出：3
        解释：最长公共子序列是 "abc"，它的长度为 3。
        """
        # str1 = 1a2b3c

        # str2 = 123abc

        #   1	a	2	b	3	c
        # 1	1	1	1	1	1	1
        # 2	1	1	2	2	2	2
        # 3	1	1	2	2	3	3
        # a	1	2	2	2	3	3
        # b	1	2	2	3	3	3
        # c	1	2	2	3	3	4
        # 从上表可以看出：

        # 当str1[i] = str2[j]时，此时的最大子序列长度应该等于左上角的值加上1（当i=0时为1，因为此时没有左上角）；

        # 当str1[i] != str2[j]时，此时的最大子序列长度为上方和左方的最大值（当i=0时直接为上方的值）
        
        # dp[i][j] 是str[i]和str[j]拥有的最大的子序列长度
        len_1 = len(text1)
        len_2 = len(text2)
        dp = [[0]*(len_2+1) for _ in range(len_1+1)]
        for i in range(len_1):
            for j in range(len_2):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return dp[-1][-1]


Solution().longestCommonSubsequence(text1="abcde", text2="ace")
