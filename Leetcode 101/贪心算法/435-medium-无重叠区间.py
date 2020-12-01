from typing import List


class Solution:
    """
    给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

    注意:

    可以认为区间的终点总是大于它的起点。
    区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
    示例 1:

    输入: [ [1,2], [2,3], [3,4], [1,3] ]

    输出: 1

    解释: 移除 [1,3] 后，剩下的区间没有重叠。
    """

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 我们首先将输入的intervals按照end排序，然后保证我们每次放入区间的end最小，也就是对于后面要加入的区间留有更多的余地。
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        len_inter = len(intervals)
        result, pre = 1, 0
        for i in range(1, len_inter):
            if intervals[i][0] >= intervals[pre][1]:
                result += 1
                pre = i

        return len_inter - result
