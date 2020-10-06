class Solution:
    """
    A message containing letters from A-Z is being encoded to numbers using the following mapping:

    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
    Given a non-empty string containing only digits, determine the total number of ways to decode it.

    Example 1:
    Input: "12"
    Output: 2
    Explanation: It could be decoded as "AB" (1 2) or "L" (12).

    Example 2:
    Input: "226"
    Output: 3
    Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
    """
    def numDecodings(self, s: str) -> int:
        # Solution 1
        # https: // blog.csdn.net / yangjingjing9 / java / article / details / 77036563
        # 1 s[i-2]和s[i-1] 两个字符是10----26之间但不包括10和20这两个数时，有两种编码方式，比如23------>[“BC”，“W”]，所以dp[i] = dp[i-1]+dp[i-2]
        # 2 s[i-2]和s[i-1] 两个字符10或20这两个数时，有一种编码方式，比如10------>[“J”], 所以dp[i] = dp[i-2]
        # 3 s[i-2]和s[i-1] 两个字符不在上述两种范围时，编码方式为零，比如27，比如01，所以dp[i] = dp[i-1]
        if s == "" or s[0] == '0': return 0
        dp = [1, 1]
        for i in range(2, len(s) + 1):
            if 10 <= int(s[i - 2:i]) <= 26 and s[i - 1] != '0':  # 编码方式为2
                dp.append(dp[i - 1] + dp[i - 2])
            elif int(s[i - 2:i]) == 10 or int(s[i - 2:i]) == 20:  # 编码方式为1
                dp.append(dp[i - 2])
            elif s[i - 1] != '0':  # 编码方式为0
                dp.append(dp[i - 1])
            else:
                return 0
        return dp[len(s)]

        # Solution 2
        # https: // blog.csdn.net / fuxuemingzhu / java / article / details / 82120874
        # 对于”226”：
        # 令dp数组为[0, 0, 0, 0]，初始化为[1, 0, 0, 0]；
        # 从第一个位置开始，输入为”2”，不为”0”，所以dp数组为[1, 1, 0, 0]；
        # 第2个位置，输入为”2”，不为”0”，所以dp数组为[1, 1, 1, 0]；此时前两位数字是”22”，满足区间，所以变为[1, 1, 2, 0]；
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            if i != 1 and '09' < s[i-2:i] < '27':
                dp[i] += dp[i-2]
        return dp[-1]

print(Solution().numDecodings("22655"))
# a="a"
# print(a[:2])