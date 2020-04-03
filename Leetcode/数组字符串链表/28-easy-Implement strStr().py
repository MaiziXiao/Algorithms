class Solution:
    """
    Implement strStr().

    Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    Example 1:
    Input: haystack = "hello", needle = "ll"
    Output: 2
    Example 2:

    Input: haystack = "aaaaa", needle = "bba"
    Output: -1

    Clarification:
    What should we return when needle is an empty string? This is a great question to ask during an interview.
    """
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        m = len(haystack)
        n = len(needle)
        for i in range(m):
            if haystack[i] == needle[0]:
                if i+n <= m:
                    if haystack[i:i+n] == needle:
                        return i
                else:
                    return -1
        return -1

print(Solution().strStr("aaaaa", "bba"))
