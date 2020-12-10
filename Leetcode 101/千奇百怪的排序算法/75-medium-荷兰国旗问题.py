from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

        此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

        进阶：

        你可以不使用代码库中的排序函数来解决这道题吗？
        你能想出一个仅使用常数空间的一趟扫描算法吗？
         

        示例 1：

        输入：nums = [2,0,2,1,1,0]
        输出：[0,0,1,1,2,2]
        Do not return anything, modify nums in-place instead.
        """
        #  解法一
        # 遍历数组，统计（0，1，2）的个数, 根据 (0，1，2）的个数重排数组 这种思路的时间复杂度：O(n)，需要遍历数组两次。

        # 解法二
        # 我们可以把数组分成三部分，前部（全部是0），中部（全部是1）和后部（全部是2）三个部分。
        # 每一个元素（红白蓝分别对应0、1、2）必属于其中之一。将前部和后部各排在数组的前边和后边，中部自然就排好了。
        # 我们用三个指针，设置两个指针begin指向前部的末尾的下一个元素（刚开始默认前部无0，所以指向第一个位置），
        # end指向后部开头的前一个位置（刚开始默认后部无2，所以指向最后一个位置），然后设置一个遍历指针current，从头开始进行遍历。
        # 这种思路的时间复杂度也是$O(n)$, 只需要遍历数组一次。


        p0 = cur = 0
        p2 = len(nums) - 1

        while cur <= p2:
            if nums[cur] == 0:
                nums[cur], nums[p0] = nums[p0], nums[cur]
                p0 += 1
                cur += 1
            elif nums[cur] == 2:
                # 和后面交换,所以cur指针不用+1
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            elif nums[cur] == 1:
                cur += 1

Solution().sortColors([2,0,2,1,1,0])