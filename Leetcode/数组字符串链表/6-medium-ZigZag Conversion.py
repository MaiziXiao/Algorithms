class Solution:
    """
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
    (you may want to display this pattern in a fixed font for better legibility)
    P   A   H   N
    A P L S I I G
    Y   I   R
    And then read line by line: "PAHNAPLSIIGYIR"
    Write the code that will take a string and make this conversion given a number of rows:
    string convert(string s, int numRows);

    Example 1:
    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"

    Example 2:
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:

    P     I    N
    A   L S  I G
    Y A   H R
    P     I
    """

    def convert(self, s: str, numRows: int) -> str:
        list = [[0 for x in range(len(s))] for y in range(numRows)]
        m, n = 0, 0
        zig_down = True
        if numRows == 1:
            return s

        for i in range(len(s)):
            print(m, n)
            list[m][n] = s[i]
            if zig_down and m < numRows - 1:
                m += 1
            elif zig_down and m == numRows - 1:
                zig_down = False
                m -= 1
                n += 1
            elif not zig_down and m > 0:
                m -= 1
                n += 1
            elif not zig_down and m == 0:
                zig_down = True
                m += 1

        res = ""
        for m in range(len(list)):
            for n in range(len(list[0])):
                if list[m][n] != 0:
                    res = res + list[m][n]
        return res

    # 发现所有行的重复周期都是 2 * nRows - 2
    # 对于首行和末行之间的行，还会额外重复一次，重复的这一次距离本周期起始字符的距离是 2 * nRows - 2 - 2 * i


print(Solution().convert("ABCasdfasdf", 2))
