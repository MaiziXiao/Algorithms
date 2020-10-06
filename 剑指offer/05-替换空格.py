class Solution:
    def replaceSpace(self, s: str) -> str:
        """
        请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
        示例 1：

        输入：s = "We are happy."
        输出："We%20are%20happy."
         

        限制：
        0 <= s 的长度 <= 10000
        """
        i = 0
        while i <= len(s)-1:
            if s[i] == " ":
                s = s[:i] + "%20" + s[i+1:]
                i += 3
            else:
                i += 1
        return s


Solution().replaceSpace("We are happy.")