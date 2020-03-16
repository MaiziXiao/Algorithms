from typing import List
class Solution:
    """
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    Example 1:
    Input: ["flower","flow","flight"]
    Output: "fl"

    Example 2:
    Input: ["dog","racecar","car"]
    Output: ""

    Explanation: There is no common prefix among the input strings.
    Note:

    All given inputs are in lowercase letters a-z.
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Solution 1
        # if not strs:
        #     return ""
        # common_prefix = strs[0]
        # strs = strs[1:]
        # for word in strs:
        #     i = 0
        #     tmp_prefix = ""
        #     while i < len(word) and i < len(common_prefix):
        #         if word[i] == common_prefix[i]:
        #             tmp_prefix += word[i]
        #         else:
        #             break
        #         i += 1
        #     common_prefix = tmp_prefix
        #     if not common_prefix:
        #         return ""
        # return common_prefix

        # Solution 2
        if not strs:
            return ''
        res = ''
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

print(Solution().longestCommonPrefix(["aca","cba"]))