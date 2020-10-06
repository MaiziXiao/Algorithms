class Solution:
    """
    Given two binary strings, return their sum (also a binary string).

    The input strings are both non-empty and contains only characters 1 or 0.

    Example 1:
    Input: a = "11", b = "1"
    Output: "100"

    Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"


    Constraints:
    Each string consists only of '0' or '1' characters.
    1 <= a.length, b.length <= 10^4
    Each string is either "0" or doesn't contain any leading zero.
    """
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        res = ""
        rest = 0

        for i in range(max(len_a,len_b)):
            if len_a-1-i >= 0:
                x = int(a[len_a-1-i])
            else:
                x = 0
            if len_b-1-i >= 0:
                y = int(b[len_b-1-i])
            else:
                y = 0

            if  x+y+rest == 0:
                res = "0"+res
                rest = 0
            elif x+y+rest == 1:
                res = "1"+res
                rest = 0
            elif x+y+rest == 2:
                res = "0"+res
                rest = 1
            elif x+y+rest == 3:
                res = "1"+res
                rest = 1

        if rest == 1:
            res = "1"+res

        return res

Solution().addBinary(a="1010", b="1011")
