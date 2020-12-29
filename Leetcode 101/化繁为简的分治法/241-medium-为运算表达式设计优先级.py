from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        """
        给定一个含有数字和运算符的字符串，为表达式添加括号，
        改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。

        示例 1:
        输入: "2-1-1"
        输出: [0, 2]
        解释:
        ((2-1)-1) = 0
        (2-(1-1)) = 2
        """
        if input.isdigit():  # 不同于Java版本，这里边界条件放在这里，之前那个是res.isEmpty()就加入数字
            return [int(input)]  # 转换成数字 -> 列表并返回
        res = []
        for i in range(len(input)):
            if input[i] in "+-*":
                L = self.diffWaysToCompute(input[:i])
                R = self.diffWaysToCompute(input[i + 1:])

                for left in L:
                    for right in R:
                        res.append(self.computer(left, right, input[i]))

        return res

    def computer(self, a, b, op):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        else:
            return a * b


print(Solution().diffWaysToCompute("2-1-1"))
