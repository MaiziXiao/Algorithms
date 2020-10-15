class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

        示例 1:

        输入: "abcabcbb"
        输出: 3
        解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
        示例 2:

        输入: "bbbbb"
        输出: 1
        解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
        示例 3:

        输入: "pwwkew"
        输出: 3
        解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
             请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
        """
        if len(s) <= 1:
            return len(s)
        longest_num = 0
        longest_string = ""
        for i in s:
            if i not in longest_string:
                longest_string += i
            else:
                longest_num = max(longest_num, len(longest_string))

                for j in range(len(longest_string)):
                    if longest_string[j] == i:
                        longest_string = longest_string[j+1:] + i
                        break

        return max(longest_num, len(longest_string))
Solution().lengthOfLongestSubstring("dvdf")
