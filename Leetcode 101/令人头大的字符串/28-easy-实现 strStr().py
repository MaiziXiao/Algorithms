class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        实现 strStr() 函数。
        给定一个 haystack 字符串和一个 needle 字符串，
        在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

        示例 1:

        输入: haystack = "hello", needle = "ll"
        输出: 2
        示例 2:

        输入: haystack = "aaaaa", needle = "bba"
        输出: -1
        """
        # 时间复杂度：O((N - L)L)，其中 N 为 haystack 字符串的长度，L 为 needle 字符串的长度。
        # 内循环中比较字符串的复杂度为 L，总共需要比较 (N - L) 次。
        # 空间复杂度：O(1)O(1)。

        L, n = len(needle), len(haystack)

        for start in range(n - L + 1):
            if haystack[start: start + L] == needle:
                return start
        return -1
