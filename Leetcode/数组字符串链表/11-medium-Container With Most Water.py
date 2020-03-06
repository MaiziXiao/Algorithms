class Solution:
    """
    Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical
    lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with
    x-axis forms a container, such that the container contains the most water.

    Note: You may not slant the container and n is at least 2.

    Example:
    Input: [1,8,6,2,5,4,8,3,7]
    Output: 49
    """
    def maxArea(self, height) -> int:
        """
        双指针从两边依次往里
        :param height:
        :return:
        """
        max_area = 0
        i = 0
        j = len(height) - 1
        while i < j:
            if height[i] < height[j]:
                area = height[i] * (j-i)
                i = i+1
            else:
                area = height[j] * (j-i)
                j = j-1
            if area > max_area:
                max_area = area
        return max_area


result = Solution().maxArea([1,8,6,2,5,4,8,3,7])
print(result)