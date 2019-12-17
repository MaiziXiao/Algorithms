class Solution:
    def removeDuplicates(self, nums):
        """
        Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
        Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

        Example 1:
        Given nums = [1,1,2],
        Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
        It doesn't matter what you leave beyond the returned length.
        """
        # 倒序不会弄乱index, Time complexity: O(n)
        for i in range(len(nums)-1, -1, -1):
            if i == 0:
                return len(nums)
            if nums[i] == nums[i-1]:
                nums.pop(i)


result = Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(result)
