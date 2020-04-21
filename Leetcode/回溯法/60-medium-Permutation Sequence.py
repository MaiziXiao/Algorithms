class Solution:
    """
    The set [1,2,3,...,n] contains a total of n! unique permutations.

    By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"
    Given n and k, return the kth permutation sequence.

    Note:
    Given n will be between 1 and 9 inclusive.
    Given k will be between 1 and n! inclusive.

    Example 1:
    Input: n = 3, k = 3
    Output: "213"
    """
    def getPermutation(self, n: int, k: int) -> str:

        # Solution 1 找规律, https://www.cnblogs.com/grandyang/p/4358678.html 找规律
        ans = ''
        fact = [1] * n
        num = [str(i) for i in range(1, 10)]
        for i in range(1, n):
            fact[i] = fact[i - 1] * i
        k -= 1
        for i in range(n, 0, -1):
            first = k // fact[i - 1]
            k %= fact[i - 1]
            ans += num[first]
            num.pop(first)
        return ans

        # Solution 2, 回溯法1, 超时
        # res = []
        # cur = ""
        # list = [i+1 for i in range(n)]
        # def dfs(list, cur):
        #     if len(cur) == n:
        #         res.append(cur)
        #         return
        #     for i in range(len(list)):
        #         dfs(list[:i]+list[i+1:], cur+str(list[i]))
        # dfs(list, cur)
        # return res[k-1]

        # Solution 3 回溯法2, 超时
        # res = []
        # cur = ""
        # list = [i+1 for i in range(n)]
        # def dfs(list, cur):
        #     if len(cur) == n:
        #         res.append(cur)
        #         return
        #     for i in range(len(list)):
        #         # 不加就不用Pop
        #         cur += str(list[i])
        #         dfs(list[:i]+list[i+1:], cur)
        #         cur = cur[:-1]
        # dfs(list, cur)
        # return res[k-1]

Solution().getPermutation(9, 62716)
