from typing import List


class Solution:
    """
    Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are
    adjacent, with the colors in the order red, white and blue.
    Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
    Note: You are not suppose to use the library's sort function for this problem.

    Example:
    Input: [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
    Follow up:
    A rather straight forward solution is a two-pass algorithm using counting sort.
    First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
    Could you come up with a one-pass algorithm using only constant space?
    """

    def sortColors(self, nums: List[int]) -> None:
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
