from typing import List

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        """
        从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，
        而大、小王为 0 ，可以看成任意数字。A 不能视为 14。


        示例1:
        输入: [1,2,3,4,5]
        输出: True

        示例2:
        输入: [0,0,1,2,5]
        输出: True
        """
        # num_zeros = 0
        # i = 0
        # while i < len(nums):
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         num_zeros += 1
        #     else:
        #         i += 1
        #
        # nums.sort()
        #
        # if num_zeros >= 4:
        #     return True
        #
        # i = 1
        # last_num = nums[0]
        # while i < len(nums):
        #     if nums[i] == last_num+1:
        #         i += 1
        #         last_num += 1
        #         continue
        #     elif num_zeros > 0:
        #         num_zeros -= 1
        #         last_num += 1
        #         continue
        #     else:
        #         return False
        # return True

        # 如果重复，肯定错误。 如果不存在0，则最大值最小值之差必定为4 其他情况，最大值最小值之差小于4即可
        num_zeros = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                num_zeros += 1
            else:
                i += 1

        nums.sort()

        last_num = -1
        for num in nums:
            if num == last_num:
                return False
            else:
                last_num = num
        if nums[-1] - nums[0] < 5:
            return True
        else:
            return False