class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        """
        字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
        比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

        示例 1：
        输入: s = "abcdefg", k = 2
        输出:"cdefgab"
        """
        # 自己做法
        return s[n:] + s[:n]

        # 原地反转
        # 我们先将 abcdefg 的前面 k 个字符和 k + 1 到末尾的字符分别翻转，得到 bagfedc ,再对这个字符串进行一次翻转，即可得到答案 cdefgab