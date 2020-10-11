class MinStack:
    """
    定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
    示例:

    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.min();   --> 返回 -3.
    minStack.pop();
    minStack.top();      --> 返回 0.
    minStack.min();   --> 返回 -2.
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.s_help = []
    # 空间换时间
    # 如果push的数小于最小值，push X到辅助栈，不然将辅助栈最后一个数再push到辅助栈里
    def push(self, x: int) -> None:
        if not self.s or x <= self.s_help[-1]:
            self.s_help.append(x)
        else:
            self.s_help.append(self.s_help[-1])
        self.s.append(x)

    def pop(self) -> None:
        self.s.pop()
        return self.s_help.pop()

    def top(self) -> int:
        return self.s[-1]

    def min(self) -> int:
        return self.s_help[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()