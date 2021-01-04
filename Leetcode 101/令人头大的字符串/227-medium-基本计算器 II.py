class Solution:
    def calculate(self, s: str) -> int:
        """
        实现一个基本的计算器来计算一个简单的字符串表达式的值。
        字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

        示例 1:
        输入: "3+2*2"
        输出: 7

        示例 2:
        输入: " 3/2 "
        输出: 1

        示例 3:
        输入: " 3+5 / 2 "
        输出: 5
        """
        # # 最简单加减法计算机
        # # 1、先给第一个数字加一个默认符号+，变成+1-12+3。
        # # 2、把一个运算符和数字组合成一对儿，也就是三对儿+1，-12，+3，把它们转化成数字，然后放到一个栈中。
        # # 3、将栈中所有的数字求和，就是原算式的结果。
        # # 处理乘除法
        # # 其实思路跟仅处理加减法没啥区别，拿字符串2-3*4+5举例，核心思路依然是把字符串分解成符号和数字的组合。
        # # 比如上述例子就可以分解为+2，-3，*4，+5几对儿，我们刚才不是没有处理乘除号吗，很简单，其他部分都不用变，在switch部分加上对应的 case 就行了：
        # # 用num保存上一个数字，用pre_op保存上一个操作符。当遇到新的操作符的时候，需要根据pre_op进行操作。乘除的优先级高于加减。所以有以下规则：
        # # 处理带括号
        # # 因为括号具有递归性质。我们拿字符串3*(4-5/2)-6举例：
        # # calculate(3*(4-5/2)-6)
        # # = 3 * calculate(4-5/2) - 6
        # # = 3 * 2 - 6
        # # = 0
        # # 可以脑补一下，无论多少层括号嵌套，通过 calculate 函数递归调用自己，都可以将括号中的算式化简成一个数字。换句话说，括号包含的算式，我们直接视为一个数字就行了。
        # stack = []
        # sign = "+"
        # num = 0
        # s = list(s)
        # while len(s) > 0:
        #     c = s.pop(0)
        #     if c.isdigit():
        #         num = 10 * num + int(c)
        #     # 当是符号或者已经到最后,处理上一个算式
        #     # +3+5/2+1,当到第二个加号时，+3入栈，第一个除号时，+5入栈，最后一个加号时，拿栈顶+5/2再入栈。到最后时，把+1入栈
        #     if (not c.isdigit() and c != " ") or len(s) == 0:
        #         if sign == "+":
        #             stack.append(num)
        #         elif sign == "-":
        #             stack.append(-num)
        #         elif sign == "*":
        #             stack[-1] = stack[-1] * num
        #         elif sign == "/":
        #             # python 除法向 0 取整的写法
        #             stack[-1] = int(stack[-1] / float(num))
        #         # 重置
        #         num = 0
        #         sign = c

        # return sum(stack)

        # 有括号的情况
        def helper(s) -> int:
            stack = []
            sign = "+"
            num = 0

            while len(s) > 0:
                c = s.pop(0)
                if c.isdigit():
                    num = 10 * num + int(c)
                # 遇到左括号开始递归计算 num
                if c == "(":
                    num = helper(s)

                if (not c.isdigit() and c != " ") or len(s) == 0:
                    if sign == "+":
                        stack.append(num)
                    elif sign == "-":
                        stack.append(-num)
                    elif sign == "*":
                        stack[-1] = stack[-1] * num
                    elif sign == "/":
                        # python 除法向 0 取整的写法
                        stack[-1] = int(stack[-1] / float(num))
                    num = 0
                    sign = c
                # 遇到右括号返回递归结果, break while, return sum(stack)
                if c == ")":
                    break
            return sum(stack)

        return helper(list(s))


Solution().calculate("3*(4-5/2)-6")
