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
        substring = []
        max_len = 0
        for letter in s:
            print(letter, substring)
            if letter not in substring:
                substring.append(letter)
                max_len = max(max_len, len(substring))
            else:
                substring = [letter]
        print(max_len)
        return max_len
Solution().lengthOfLongestSubstring("dvdf")