import string
class Solution:
    def translateNum(self, num: int) -> int:
        """
        给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11
        翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

        示例 1:

        输入: 12258
        输出: 5
        解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
        """
        mapping = {str(i): string.ascii_lowercase[i] for i in range(26)}
        num = str(num)

        def dp(s: str):
            print(s)
            if len(s) == 1:
                return 1
            if len(s) == 2:
                # i.e. 23可以变成 2，3和23
                if s in mapping:
                    return 2
                # i.e. 59只能变成5和9
                else:
                    return 1
            if s[:2] in mapping:
                return dp(s[1:]) + dp(s[2:])
            else:
                return dp(s[1:])
        return dp(num)

print(Solution().translateNum(624))