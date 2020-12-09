# 选择排序
# https://blog.csdn.net/Hk_john/article/details/79888992
# # 平均时间复杂度为：O(n*n) 空间复杂度：O(1)

# 初始状态：无序区为R[1..n]，有序区为空；
# 第i趟排序(i=1,2,3…n-1)开始时，当前有序区和无序区分别为R[1..i-1]和R(i..n）。
# 该趟排序从当前无序区中-选出关键字最小的记录 R[k]，将它与无序区的第1个记录R交换，使R[1..i]和R[i+1..n)
# 分别变为记录个数增加1个的新有序区和记录个数减少1个的新无序区；
# n-1趟结束，数组有序化了。


def selectSort(arr):
    length = len(arr)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


arr = [64, 34, 25, 12, 22, 11, 90]

selectSort(arr)

print("排序后的数组:")
for i in range(len(arr)):
    print("%d" % arr[i])
