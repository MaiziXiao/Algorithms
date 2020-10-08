class CQueue:
    """
    用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
    分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

    示例 1：

    输入：
    ["CQueue","appendTail","deleteHead","deleteHead"]
    [[],[3],[],[]]
    输出：[null,null,3,-1]

    示例 2：
    输入：
    ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
    [[],[],[5],[2],[],[]]
    输出：[null,-1,null,null,5,2]
    提示：

    1 <= values <= 10000
    最多会对 appendTail、deleteHead 进行 10000 次调用
    """
    # 先进来的数字，首先显示出来了，但是题目中说要使用栈，栈是先进后出的，使用栈来实现先进先出
    # 在这里使用两个栈就好了，从一个进来再到另一个栈，这样顺序就是先进先出了。题目的主旨写在第一句，就是，使用两个栈实现一个队列。
    def __init__(self):
        self.stackin=[]
        self.stackout=[]

    def appendTail(self, value: int) -> None:
        self.stackin.append(value)

    def deleteHead(self) -> int:
        # stack1用来存元素，stack2用来出元素。
        # 每次要出队首元素的时候，先看stack2是否还有元素，有就出；
        # 没有就看stack1中有没有元素，没有就返回-1
        # 有就把stack1的元素全部搬到stack2（顺序相反）
        if self.stackout:
            return self.stackout.pop()
        elif not self.stackin:
            return -1
        else:
            while self.stackin:
                self.stackout.append(self.stackin.pop())
            return self.stackout.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()