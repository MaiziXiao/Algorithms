from typing import List
class Solution:
    """
    Given a string containing only digits, restore it by returning all possible valid IP address combinations.

    Example:
    Input: "25525511135"
    Output: ["255.255.11.135", "255.255.111.35"]
    """
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        cur = ""

        def dfs(cur, left, split):
            if left == "" and split == 4:
                # 去掉最后一个.
                res.append(cur[:-1])
            if split > 4 or not left:
                return
            # IP 地址最多3位
            # 一位的时候, 0-9都可以

            dfs(cur+"{}.".format(left[0]), left[1:], split+1)
            # 二位的时候, 10-99
            if "10" <= left[:2] <= "99" and len(left) >= 2:
                dfs(cur+"{}.".format(left[:2]), left[2:], split+1)
            # 小心! string长度为2时, s[:3]不会报错,所以不判断string长度的话会重复
            if "100" <= left[:3] <= "255" and len(left) >= 3:
                dfs(cur+"{}.".format(left[:3]), left[3:], split+1)
        dfs(cur, s, 0)

        return res

print(Solution().restoreIpAddresses("101023"))

