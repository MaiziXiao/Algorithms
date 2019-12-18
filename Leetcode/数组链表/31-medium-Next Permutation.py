class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
        If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
        The replacement must be in-place and use only constant extra memory.

        Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
        字典序
        1,2,3 → 1,3,2
        3,2,1 → 1,2,3
        1,1,5 → 1,5,1
        Do not return anything, modify nums in-place instead.
        i.e.
        6 5 4 8 8 7 5 1
        首先肯定从后面开始看，1和5调换了没有用。7、5和1调换了也没有效果，因此而发现了8、7、5、1是递减的。
        """
        #　从后往前递增的话第一个不再增大的数
        for i in range(len(nums)-1, 0, -1):
            # 从后往前第一个不再递增的数
            if nums[i] >= nums[i-1]:
                j = len(nums) - 1
                # 从后往前找比nums[i-1]大最少的数，万一找不到说明这个list是字典序最后一个，reverse
                while j >= i:
                    if nums[j] > nums[i-1]:
                        # 交换nums[i-1]和从后往前比nums[i-1]大最少的数, i-1之后的数递减，最多只要9次
                        tmp = nums[i-1]
                        nums[i-1] = nums[j]
                        nums[j] = tmp
                        # sort i 到最后的数
                        sub_list = nums[i:len(nums)]
                        sub_list.sort()
                        nums[i:len(nums)] = sub_list
                        return nums
                    j -= 1
        nums.reverse()
        return nums

# result = Solution().nextPermutation([6,5,4,8,8,7,5,1])
result = Solution().nextPermutation([5, 1, 1])
print(result)