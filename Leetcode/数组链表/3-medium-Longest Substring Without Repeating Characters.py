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
        left, right = 0, 0
        subString = []
        res = 0
        while left < len(s) and right < len(s):
            if s[right] not in subString:
                subString.append(s[right])
                right += 1
            else:
                subString.pop(0)
                left += 1
            res = max(res, len(s))
        return res


print(Solution().lengthOfLongestSubstring("dvdf"))