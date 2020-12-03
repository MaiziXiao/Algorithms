from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

        注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。

        示例 1：

        输入：s = "ADOBECODEBANC", t = "ABC"
        输出："BANC"
        示例 2：

        输入：s = "a", t = "a"
        输出："a"
        """
        mem = defaultdict(int)
        for char in t:
            mem[char] += 1
        t_len = len(t)

        minLeft, minRight = 0, len(s)
        left = 0
        # 移动右指针
        for right, char in enumerate(s):
            if mem[char] > 0:
                t_len -= 1
            mem[char] -= 1
            # 如果满足，移动左指针
            if t_len == 0:
                while mem[s[left]] < 0:
                    mem[s[left]] += 1
                    left += 1

                if right - left < minRight - minLeft:
                    minLeft, minRight = left, right

                mem[s[left]] += 1
                t_len += 1
                left += 1
        return "" if minRight == len(s) else s[minLeft : minRight + 1]  # noqa:E203


Solution().minWindow(s="ADOBECODEBANC", t="ABC")
