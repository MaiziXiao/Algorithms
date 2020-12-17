class Solution:
    def numDecodings(self, s: str) -> int:
        """
        一条包含字母 A-Z 的消息通过以下方式进行了编码：

        'A' -> 1
        'B' -> 2
        ...
        'Z' -> 26
        给定一个只包含数字的非空字符串，请计算解码方法的总数。

        题目数据保证答案肯定是一个 32 位的整数。

         

        示例 1：

        输入：s = "12"
        输出：2
        解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
        """
        # 像走阶梯问题，dp[i]和dp[i-1]和dp[i-2]相关，需要考虑corner case,
        # 如果s[i]是0， dp[i] = dp[i-2]
        # 不是0, 10<s[i-2: i]<26: dp[i] = dp[i-2]+dp[i-1] 不然dp[i] = dp[i-1]

        # https://zhenyu0519.github.io/2020/02/20/lc91/
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            if int(s[i-1]) != 0:
                dp[i] = dp[i-1]
            if i != 1 and '09' < s[i-2:i] < '27':
                dp[i] += dp[i-2]
        return dp[-1]


Solution().numDecodings("2101")
