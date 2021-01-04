class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

        示例 1:
        输入: s = "anagram", t = "nagaram"
        输出: true

        示例 2:
        输入: s = "rat", t = "car"
        输出: false
        """
        freq = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if freq.get(s[i]):
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1

        for j in range(len(t)):
            if freq.get(t[j]) and freq[t[j]] > 0:
                freq[t[j]] -= 1

        for value in freq.values():
            if value != 0:
                return False
        return True


Solution().isAnagram(s="anagram", t="nagaram")
