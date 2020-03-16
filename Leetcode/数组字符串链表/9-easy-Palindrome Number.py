class Solution:
    """
    Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

    Example 1:
    Input: 121
    Output: true

    Example 2:
    Input: -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

    Example 3:
    Input: 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    """
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        left = 0
        right = len(num_str)-1
        while left < right:
            if num_str[left] == num_str[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

Solution().isPalindrome(121)