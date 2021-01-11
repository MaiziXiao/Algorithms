from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

        例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

        提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
        """
        # 比对当前元素与栈顶元素的大小
        # 若当前元素 < 栈顶元素：入栈
        # 若当前元素 > 栈顶元素：弹出栈顶元素，记录两者下标差值即为所求天数

        #  73入栈，74>73，73出栈，74入栈，74使得73出栈，所以73需要等待1-0=1天 ，栈内元素74.
        # 75入栈，75>74, 74出栈，75入栈，75使得74出栈，所以74需要等待2-1=1天，栈内元素75.
        # 71入栈，71<75，直接入栈，栈内元素 75,71
        # 69直接入栈，栈内元素75,71,69

        res = [0] * len(T)
        stack = []
        for i in range(len(T)):
            if not stack or T[i] <= stack[-1][1]:
                stack.append([i, T[i]])
            else:
                while stack and T[i] > stack[-1][1]:
                    index, temp = stack.pop()
                    res[index] = i - index
                stack.append([i, T[i]])
        return res


Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
