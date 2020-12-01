class Solution:
    """
    Given a string, find the length of the longest substring without repeating characters.

    Example 1:
    Input: "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Example 2:
    Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    Example 3:
    Input: "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
                 Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 虫取法
        # left, right = 0, 0
        # subString = []
        # res = 0
        # while left < len(s) and right < len(s):
        #     print(subString)
        #     if s[right] not in subString:
        #         subString.append(s[right])
        #         right += 1
        #     else:
        #         subString.pop(0)
        #         left += 1
        #     res = max(res, len(subString))
        # return res
        # 哈希表法
        left, right = 0, 0
        res = 0
        letter_dict = {}
        while right < len(s):
            if s[right] not in letter_dict:
                letter_dict[s[right]] = right
            else:
                # 对于abba，当right指向最后的a的时候，left指向的是字典中保留的有第一个位置的a，如果不对此进行判断的话，left会移动到第一个字符b。
                left = max(left, letter_dict[s[right]] + 1)
                letter_dict[s[right]] = right
            right += 1
            res = max(res, len(s[left:right]))
        return res

print(Solution().lengthOfLongestSubstring("abba"))