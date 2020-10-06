class Solution:
    """
    Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last
    word (last word means the last appearing word if we loop from left to right) in the string.
    If the last word does not exist, return 0.

    Note: A word is defined as a maximal substring consisting of non-space characters only.

    Example:
    Input: "Hello World"
    Output: 5
    """
    def lengthOfLastWord(self, s: str) -> int:
        res = ""
        last_blank = False
        for i in s:
            if i == " ":
                last_blank = True
            else:
                if last_blank:
                    res = ""
                    last_blank = False
                res += i
        return len(res)

print(Solution().lengthOfLastWord("Hello World"))