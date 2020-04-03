from typing import List

class Solution:
    """
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    For example, given n = 3, a solution set is:
    [
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"
    ]
    """
    def generateParenthesis(self, n: int) -> List[str]:

        if n == 0:
            return None

        def dfs(cur, num_left_brackets, num_right_brackets):
            if num_left_brackets == n and num_right_brackets == n:
                ans.append(cur)
                return
            else:
                if num_left_brackets < n:
                    dfs(cur+"(", num_left_brackets+1, num_right_brackets)
                if num_left_brackets > num_right_brackets:
                    dfs(cur+")", num_left_brackets, num_right_brackets+1)

        cur = ""
        ans = []
        dfs(cur, 0, 0)
        return ans

print(Solution().generateParenthesis(3))