class Solution:
    def search(self, nums, target):
        """
        Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
        (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
        You are given a target value to search. If found in the array return its index, otherwise return -1.
        You may assume no duplicate exists in the array.
        Your algorithm's runtime complexity must be in the order of O(log n).

        Example 1:
        Input: nums = [4,5,6,7,0,1,2], target = 0
        Output: 4
        """
        # Binary Search with index shift
        low = 0
        height = len(nums) - 1
        while low <= height:
            mid = (height - low) // 2 + low
            if nums[mid] == target:
                return mid
            elif nums[low] == target:
                return low
            elif nums[height] ==target:
                return height

            # 有序部分在左边
            if nums[mid] > nums[low]:
                if nums[low] < target < nums[mid]:
                    height = mid - 1
                else:
                    low = mid + 1
            # 有序部分在右边
            else:
                if nums[mid] < target < nums[height]:
                    low = mid + 1
                else:
                    height = mid - 1

        return -1


result = Solution().search([1] ,1)
print(result)
# result = Solution().search([0,1,2,4,5,6,7] ,5)