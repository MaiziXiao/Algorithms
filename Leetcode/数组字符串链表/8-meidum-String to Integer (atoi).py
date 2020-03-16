class Solution:
    """
    Implement atoi which converts a string to an integer.

    The function first discards as many whitespace characters as necessary until the first non-whitespace character is
    found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical
     as possible, and interprets them as a numerical value.

    The string can contain additional characters after those that form the integral number, which are ignored and have
    no effect on the behavior of this function.

    If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence
    exists because either str is empty or it contains only whitespace characters, no conversion is performed.

    If no valid conversion could be performed, a zero value is returned.

    Note:
    Only the space character ' ' is considered as whitespace character.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer
    range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or
    INT_MIN (−231) is returned.

    Example 1:
    Input: "42"
    Output: 42

    Example 2:
    Input: "   -42"
    Output: -42
    Explanation: The first non-whitespace character is '-', which is the minus sign.
                 Then take as many numerical digits as possible, which gets 42.

    Example 4:
    Input: "words and 987"
    Output: 0
    Explanation: The first non-whitespace character is 'w', which is not a numerical
                 digit or a +/- sign. Therefore no valid conversion could be performed.

    """

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0
        ans = []
        ch = str[0]
        if ch == "-":
            c = -1
        elif ch == "+":
            c = 1
        elif ch.isdigit():
            ans.append(ch)
            c = 1
        else:
            return 0
        for ch in str[1:]:
            if ch.isdigit():
                ans.append(ch)
            else:
                break
        ans_str = "".join(ans)
        if ans_str:
            ans = c * int(ans_str)
            if ans > 2147483647:
                return 2147483647
            elif ans < -2147483648:
                return -2147483648
            else:
                return ans
        else:
            return 0

print(Solution().myAtoi("0-1"))