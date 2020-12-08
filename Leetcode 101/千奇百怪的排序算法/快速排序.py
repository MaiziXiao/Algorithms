# 快速排序
# https://blog.csdn.net/Hk_john/article/details/79888992
# https://zhuanlan.zhihu.com/p/63227573
# 平均时间复杂度为：O(nlogn)

# 快速排序使用分治法来把一个串（list）分为两个子串（sub-lists）。具体算法描述如下：
# 从数列中挑出一个元素，称为 “基准”（pivot）；
# 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
# 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。


def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    # 从数列中挑出一个元素，称为 “基准”（pivot）；
    key = array[low]
    while left < right:
        # 先从右边
        # 如果大于基准值，留在原地，把右指针往左一个
        while left < right and array[right] > key:
            right -= 1
        # 小于基准值，把右指针的值放到左边去 （因为基准被存在key里了，所以可以In place）
        array[left] = array[right]
        # 先从右边
        # 如果小于基准值，留在原地，把左指针往右一个
        while left < right and array[left] <= key:
            left += 1
        # 大于基准值，把做指针的值放到右边去
        array[right] = array[left]
    array[right] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)


lists = [30, 24, 5, 58, 18, 36, 12, 42, 39]
print("排序前的序列为：")
for i in lists:
    print(i, end=" ")
print("\n排序后的序列为：")
for i in quick_sort(lists, 0, len(lists) - 1):
    print(i, end=" ")
