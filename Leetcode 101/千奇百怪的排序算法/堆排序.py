# 堆排序
# https://blog.csdn.net/Hk_john/article/details/79888992
# 堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。
# 堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。

# 堆是一种非线性结构，可以把堆看作一个数组，也可以被看作一个完全二叉树，通俗来讲堆其实就是利用完全二叉树的结构来维护的一维数组

# 按照堆的特点可以把堆分为大顶堆和小顶堆

# 大顶堆：每个结点的值都大于或等于其左右孩子结点的值

# 小顶堆：每个结点的值都小于或等于其左右孩子结点的值

# 将初始待排序关键字序列(R1,R2….Rn)构建成大顶堆，此堆为初始的无序区；
# 将堆顶元素R[1]与最后一个元素R[n]交换，此时得到新的无序区(R1,R2,……Rn-1)和新的有序区(Rn),且满足R[1,2…n-1]<=R[n]；
# 由于交换后新的堆顶R[1]可能违反堆的性质，因此需要对当前无序区(R1,R2,……Rn-1)调整为新堆，然后再次将R[1]与无序区最后一个元素交换，
# 得到新的无序区(R1,R2….Rn-2)和新的有序区(Rn-1,Rn)。不断重复此过程直到有序区的元素个数为n-1，则整个排序过程完成。