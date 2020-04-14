class Solution:
    """
    Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

    Example 1:
    Input: num1 = "2", num2 = "3"
    Output: "6"

    Example 2:
    Input: num1 = "123", num2 = "456"
    Output: "56088"

    Note:
    The length of both num1 and num2 is < 110.
    Both num1 and num2 contain only digits 0-9.
    Both num1 and num2 do not contain any leading zero, except the number 0 itself.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.
    """
    # https://blog.csdn.net/XX_123_1_RJ/article/details/81431630
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))  # 初始化，存放乘积的数组
        pos = len(res) - 1

        for n1 in reversed(num1):
            tempPos = pos
            for n2 in reversed(num2):
                res[tempPos] += int(n1) * int(n2)
                res[tempPos - 1] += res[tempPos] // 10  # 进位
                res[tempPos] %= 10  # 取余
                tempPos -= 1
            pos -= 1

        st = 0
        while st < len(res) - 1 and res[st] == 0:  # 统计前面有几个0
            st += 1
        return ''.join(map(str, res[st:]))  # 去掉0，然后变成字符串，并返回
