class Solution:
    def firstUniqChar(self, s: str) -> str:
        """
        在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

        示例:
        s = "abaccdeff"
        返回 "b"

        s = ""
        返回 " "
        """
        duplicated = []
        not_yet_duplicated = []
        for i in s:
            if i in duplicated:
                continue
            if i not in not_yet_duplicated:
                not_yet_duplicated.append(i)
            else:
                not_yet_duplicated.pop(not_yet_duplicated.index(i))
                duplicated.append(i)
        if not_yet_duplicated:
            return not_yet_duplicated[0]
        else:
            return " "

        #         dct = {}
        #         for c in s:
        #             if c not in dct:
        #                 dct[c] = 1
        #             else:
        #                 dct[c] += 1
        #         for c in s:
        #             if dct[c] == 1:
        #                 return c
        #         return " "

Solution().firstUniqChar("leetcode")