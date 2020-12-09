# 冒泡排序
# https://blog.csdn.net/Hk_john/article/details/79888992
# # 平均时间复杂度为：O(n*n) 空间复杂度：O(1)

# 比较相邻的元素。如果第一个比第二个大，就交换它们两个；
# 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
# 针对所有的元素重复以上的步骤，除了最后一个；
# 重复步骤1~3，直到排序完成。


def bubbleSort(arr):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("排序后的数组:")
for i in range(len(arr)):
    print("%d" % arr[i])
