from typing import List
class Solution:
    """
    Given a collection of intervals, merge all overlapping intervals.

    Example 1:
    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

    Example 2:
    Input: [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.
    NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """先排序，后合并"""
        # Solution 1
        if len(intervals) <= 1:
            return intervals

        # List.sort(key=..., reverse=...)
        # reverse - If true, the sorted list is reversed (or sorted in Descending order)
        # key - function that serves as a key for the sort comparison)

        # Sort by first element
        intervals.sort(key=lambda a: a[0])

        i = 0
        while i < len(intervals)-1:
            # 前一个list的右边比后一个list左边大, merge
            if intervals[i+1][0] <= intervals[i][1]:
                # merge
                intervals[i] = [intervals[i][0], max(intervals[i][1], intervals[i+1][1])]
                intervals.pop(i+1)
            else:
                i += 1
        return intervals

        # Solution 2
        # res = []
        # left = intervals[0][0]
        # right = intervals[0][1]
        # for index in range(1, len(intervals)):
        #     print(left, right, intervals[index][0], intervals[index][1])
        #     # 对现在的list,把左边的边界和储存的右边值比较
        #     if intervals[index][0] <= right:
        #         right = intervals[index][1]
        #         print("merge")
        #     else:
        #         res.append([left, right])
        #         left = intervals[index][0]
        #         right = intervals[index][1]
        # res.append([left, right])
        # return res

print(Solution().merge([[2,6], [8,10], [15,18], [1,3]]))
