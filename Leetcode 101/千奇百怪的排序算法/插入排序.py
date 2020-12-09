# 插入排序
# https://blog.csdn.net/Hk_john/article/details/79888992
# https://blog.csdn.net/u014745194/article/details/72783257
# # 平均时间复杂度为：O(n*n) 空间复杂度：O(1)

# 一般来说，插入排序都采用in-place在数组上实现。具体算法描述如下：

# 从第一个元素开始，该元素可以认为已经被排序；
# 取出下一个元素，在已经排序的元素序列中从后向前扫描；
# 如果该元素（已排序）大于新元素，将该元素移到下一位置；
# 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
# 将新元素插入到该位置后；
# 重复步骤2~5。


def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    # 从第一个元素开始，该元素可以认为已经被排序
    for j in range(1, n):
        # 取出下一个元素，在已经排序的元素序列中从后向前扫描；
        for i in range(j, 0, -1):
            # 如果比前面的元素小，则往前移动
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
            # 否则代表比前面的所有元素都小，不需要再移动,break for 循环
            else:
                break


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("原列表为：%s" % alist)
    insert_sort(alist)
    print("新列表为：%s" % alist)
