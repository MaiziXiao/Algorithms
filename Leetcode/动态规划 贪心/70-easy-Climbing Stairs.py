class Solution:
    """

    You are climbing a stair case. It takes n steps to reach to the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    Note: Given n will be a positive integer.

    Example 1:
    Input: 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

    Example 2:
    Input: 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
    """
    def climbStairs(self, n: int) -> int:
        maps = {1:1, 2:2}

        def dp(k):
            if maps.get(k-1):
                a = maps[k-1]
            else:
                a = dp(k-1)
                maps[k-1] = a
            if maps.get(k-2):
                b = maps[k-2]
            else:
                b = maps[k-2]
                maps[k-2] = b
            return a+b

        if n == 0 or n == 1 or n == 2:
            return n

        return dp(n)

print(Solution().climbStairs(100))