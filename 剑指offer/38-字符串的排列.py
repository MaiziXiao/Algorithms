from typing import List

class Solution:
    def permutation(self, s: str) -> List[str]:
        """
        输入一个字符串，打印出该字符串中字符的所有排列。

        你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

        示例:

        输入：s = "abc"
        输出：["abc","acb","bac","bca","cab","cba"]
        """
        if len(s) == 0:
            return []
        res = []

        def dfs(s, cur):
            if len(s) == 0:
                res.append(cur)

            seen_letter = []
            for i in range(len(s)):
                if s[i] not in seen_letter:
                    seen_letter = seen_letter + [s[i]]
                    dfs(s[:i] + s[i + 1:], cur + s[i])

        dfs(s, "")

        return res