class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        给定两个字符串 s 和 t，判断它们是否是同构的。
        如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
        每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。
        不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

        示例 1:
        输入：s = "egg", t = "add"
        输出：true

        示例 2：
        输入：s = "foo", t = "bar"
        输出：false
        """
        if len(s) != len(t):
            return False
        mapping = {}
        for i in range(len(s)):
            # Already in the mapping
            if mapping.get(s[i]):
                if t[i] != mapping[s[i]]:
                    return False
            # Not yet in the mapping
            else:
                # 已经被其他字符映射
                if t[i] in list(mapping.values()):
                    return False
                else:
                    mapping[s[i]] = t[i]
        return True


Solution().isIsomorphic(s="foo", t="bar")
