class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

        具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

        示例 1：
        输入："abc"
        输出：3
        解释：三个回文子串: "a", "b", "c"

        示例 2：
        输入："aaa"
        输出：6
        解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
        """

        # s[i:j] 什么时候是回文？（dp[i][j]为 true），我们罗列一下：
        # 由单个字符组成。（见上图打钩的格子）
        # 由 2 个字符组成，且字符要相同。（1、2 是不需要用到递推公式的 base case）
        # 由超过 2 个字符组成，首尾字符相同，且剩余子串是一个回文串。（状态转移方程）
        # 链接：https://leetcode-cn.com/problems/palindromic-substrings/solution/shou-hua-tu-jie-dong-tai-gui-hua-si-lu-by-hyj8/
        # 动态规划 O(n^2) space O(n^2)
        # length = len(s)
        # result = 0
        # dp = [[False] * length for _ in range(length)]
        # for column in range(length):
        #     for row in range(column, -1, -1):
        #         # 单个字符肯定True, 或两个字符且字符相同
        #         if row == column or (column - row == 1 and s[row] == s[column]):
        #             dp[row][column] = True
        #             result += 1
        #         # 超过两个字符，首尾相同，且dp[i+1][j-1]==True
        #         elif s[row] == s[column] and dp[row + 1][column - 1]:
        #             dp[row][column] = True
        #             result += 1
        # return result

        # 中心拓展法
        # 枚举回文中心的是 O(n)O(n) 的，对于每个回文中心拓展的次数也是 O(n)O(n) 的，所以时间复杂度是 O(n^2)O(n 2)。
        result = 0
        for i in range(len(s)):
            search_start_end = [[i, i]]
            result += 1
            if i + 1 < len(s) and s[i] == s[i + 1]:
                search_start_end.append([i, i + 1])
                result += 1
            for left, right in search_start_end:
                while left - 1 >= 0 and right + 1 < len(s):
                    if s[left - 1] == s[right + 1]:
                        result += 1
                        left -= 1
                        right += 1
                    else:
                        break

        return result


Solution().countSubstrings("aaa")
