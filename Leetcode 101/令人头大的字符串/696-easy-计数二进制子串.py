class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。
        重复出现的子串要计算它们出现的次数。

        示例 1 :
        输入: "00110011"
        输出: 6
        解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

        请注意，一些重复出现的子串要计算它们出现的次数。

        另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
        """
        result = 0
        # mapping = {"0": "1", "1": "0"}
        for i in range(len(s) - 1):
            left, right = i, i + 1
            if s[left] == s[right]:
                continue
            result += 1
            while left - 1 >= 0 and right + 1 < len(s):
                if s[left - 1] == s[left] and s[right] == s[right + 1]:
                    result += 1
                    left -= 1
                    right += 1
                else:
                    break

        return result


Solution().countBinarySubstrings("00110011")
