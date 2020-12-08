# 归并排序
# https://blog.csdn.net/Hk_john/article/details/79888992
# https://www.cnblogs.com/pythonbao/p/10800699.html
# 始终都是O(nlogn）的时间复杂度。代价是需要额外的内存空间。

# 分治法
# step1 分解：将原问题分解为若干个规模较小，相互独立，与原问题形式相同的子问题；
# step2 解决：若子问题规模较小而容易被解决则直接解，否则递归地解各个子问题
# step3 合并：将各个子问题的解合并为原问题的解。

# 把长度为n的输入序列分成两个长度为n/2的子序列；
# 对这两个子序列分别采用归并排序；
# 将两个排序好的子序列合并成一个最终的排序序列。
def merge(left, right):
    res = []
    while left and right:
        min_val = left.pop(0) if left[0] < right[0] else right.pop(0)
        res.append(min_val)
    res += left if left else right
    return res


def merge_sort(A):
    if len(A) <= 1:
        res = A
    else:
        mid = len(A) // 2
        # 分，把长度为n的输入序列分成两个长度为n/2的子序列；
        left, right = merge_sort(A[:mid]), merge_sort(A[mid:])
        # 合，将两个排序好的子序列合并成一个最终的排序序列。
        res = merge(left, right)
    return res


merge_sort([11, 99, 33, 69, 77, 88, 55, 11, 33, 36, 39, 66, 44, 22])
