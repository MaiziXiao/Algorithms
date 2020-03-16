class Solution:
    """

    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    """
    def romanToInt(self, s: str) -> int:
        mapping = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = 0
        i = 0
        while i < len(s)-1:
            print(result)
            if s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X"):
                result = result - mapping[s[i]]
            elif s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C"):
                result = result - mapping[s[i]]
            elif s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"):
                result = result - mapping[s[i]]
            else:
                result += mapping[s[i]]
            i += 1
        result += mapping[s[i]]
        return result
print(Solution().romanToInt("IV"))