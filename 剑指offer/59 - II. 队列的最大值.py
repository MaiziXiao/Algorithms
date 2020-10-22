class MaxQueue:
    """
    请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
    若队列为空，pop_front 和 max_value需要返回 -1
    """
    # max_queue和queue同一长度
    def __init__(self):
        self.queue = []       # 输入队列
        self.max_queue = []   # 可能最大值队列

    def max_value(self) -> int:
        if len(self.max_queue) == 0:
            return -1
        else:
            return self.max_queue[0]

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        if not self.max_queue:
            self.max_queue.append(value)
        elif self.queue[-1] > self.max_queue[0]:
            self.max_queue = [self.queue[-1] for _ in range(len(self.queue))]
        else:
            self.max_queue.append(value)

    def pop_front(self) -> int:
        if len(self.max_queue) == 0:
            return -1
        a = self.queue.pop(0)
        self.max_queue.pop(0)
        return a

        # maxq是递减数列
        # 定义两个队列，A 队列存放的是输入的队列，B 队列存放的是可能的最大值队列。
        # 例如输入 [2,3,1,2,6,2,5,1] 队列，首先先输入个 2，那么 A 队列里就有 2，B 队列里也是2。
        # 然后是输入 3，A 队列就有 [2,3]，B 队列里的 2 比 3 小，所以就要把 B 队列清空并赋值 3。
        # 接下来输入 1，A = [2,3,1]，B队列就要考虑了，因为 1 比 3 小，说明当 A 队列里的 3 出队列之后，后面的 1 有可能是最大值，所以我们要把 1 加入到 B 队列里，接下来依次进行，会发现 B 队列永远都是按照从大到小排序好的。
        # 所以，当我们需要 pop_front A队列的时候，就需要比较 A 队列里的第一个元素和 B 队列里的第一个元素，如果相等，删除 B 队列里的头部元素。
        def __init__(self):
            self.queue = []
            self.maxq = []

        def max_value(self) -> int:
            if not self.maxq:
                return -1
            return self.maxq[0]

        def push_back(self, value: int) -> None:
            self.queue.append(value)

            while self.maxq and self.maxq[-1] < value:
                self.maxq.pop()
            self.maxq.append(value)

        def pop_front(self) -> int:
            if not self.queue:
                return -1
            v = self.queue.pop(0)
            if v == self.maxq[0]:
                self.maxq.pop(0)
            return v

        # Your MaxQueue object will be instantiated and called as such:
        # obj = MaxQueue()
        # param_1 = obj.max_value()
        # obj.push_back(value)
        # param_3 = obj.pop_front()